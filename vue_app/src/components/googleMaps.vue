<template>
    <div ref="googleMap" class="google-map"></div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

export default {
    name: 'GoogleMapsComponent',
    props: {
        zipCode: String,
        mapOptions: {
            type: Object,
            default: () => ({
                zoom: 10
            }),
        },
        authToken: String,
    },
    data() {
        return {
            map: null,
            polygons: [
                {
                    coords: [
                        { lat: 36.1586, lng: -79.9402 },
                        { lat: 36.1666, lng: -79.9302 },
                        { lat: 36.1726, lng: -79.9202 },
                        { lat: 36.1786, lng: -79.9102 },
                        { lat: 36.1746, lng: -79.9002 },
                        { lat: 36.1686, lng: -79.8902 },
                        { lat: 36.1606, lng: -79.9002 },
                        { lat: 36.1546, lng: -79.9102 },
                        { lat: 36.1506, lng: -79.9202 },
                        { lat: 36.1466, lng: -79.9302 }
                    ],
                    color: '#0000FF'
                },
                {
                    coords: [
                        { lat: 36.1126, lng: -79.7901 },
                        { lat: 36.1206, lng: -79.7821 },
                        { lat: 36.1286, lng: -79.7701 },
                        { lat: 36.1346, lng: -79.7601 },
                        { lat: 36.1386, lng: -79.7501 },
                        { lat: 36.1366, lng: -79.7401 },
                        { lat: 36.1306, lng: -79.7501 },
                        { lat: 36.1226, lng: -79.7601 },
                        { lat: 36.1166, lng: -79.7701 },
                        { lat: 36.1106, lng: -79.7801 }
                    ],
                    color: '#99CC00'
                },
                {
                    coords: [
                        { lat: 36.0723, lng: -79.7910 },
                        { lat: 36.0783, lng: -79.7810 },
                        { lat: 36.0823, lng: -79.7710 },
                        { lat: 36.0803, lng: -79.7610 },
                        { lat: 36.0743, lng: -79.7710 },
                        { lat: 36.0703, lng: -79.7810 },
                        { lat: 36.0663, lng: -79.7910 }
                    ],
                    color: '#66CC66'
                },
                {
                    coords: [
                        { lat: 36.0227, lng: -79.8195 },
                        { lat: 36.0307, lng: -79.8095 },
                        { lat: 36.0387, lng: -79.7995 },
                        { lat: 36.0347, lng: -79.7895 },
                        { lat: 36.0287, lng: -79.7995 },
                        { lat: 36.0227, lng: -79.8095 }
                    ],
                    color: '#339933'
                },
                {
                    coords: [
                        { lat: 36.0826, lng: -79.6900 },
                        { lat: 36.0906, lng: -79.6800 },
                        { lat: 36.0986, lng: -79.6700 },
                        { lat: 36.0946, lng: -79.6600 },
                        { lat: 36.0886, lng: -79.6700 },
                        { lat: 36.0826, lng: -79.6800 }
                    ],
                    color: '#FF0000'
                }
            ]
        };
    },
    watch: {
        zipCode: {
            immediate: true,
            handler(newVal) {
                if (newVal) {
                    this.getLatLngFromZipCode(newVal).then(coords => {
                        this.initMap(coords);
                    }).catch(error => console.error('Error getting location from zip code:', error));
                }
            }
        }
    },
    computed: {
        ...mapState(['userToken']),
    },
    mounted() {
        this.loadGoogleMapsScript().then(() => {
            this.initMap().then(() => {
                this.fetchAndDisplayPins();
                this.drawPolygons();
            });
        }).catch(error => console.error('Google Maps API script not loaded:', error));
    },
    methods: {
        getLatLngFromZipCode(zipCode) {
            const apiKey = '';
            const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${zipCode}&key=${apiKey}`;
            return axios.get(url)
                .then(response => {
                    const { lat, lng } = response.data.results[0].geometry.location;
                    return { lat, lng };
                })
                .catch(error => {
                    throw new Error('No results found: ' + error);
                });
        },
        drawPolygons() {
            this.polygons.forEach(polygon => {
                const mapPolygon = new google.maps.Polygon({
                    paths: polygon.coords,
                    strokeColor: polygon.color,
                    strokeOpacity: 0.8,
                    strokeWeight: 2,
                    fillColor: polygon.color,
                    fillOpacity: 0.35,
                    clickable: false
                });
                mapPolygon.setMap(this.map);
            });
        },
        loadGoogleMapsScript() {
            const apiKey = ''; // Your API key here
            return new Promise((resolve, reject) => {
                if (window.google && window.google.maps) {
                    resolve();
                } else {
                    const script = document.createElement('script');
                    script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&callback=initMap`;
                    script.async = true;
                    script.defer = true;
                    document.head.appendChild(script);
                    window.initMap = () => {
                        resolve();
                        delete window.initMap;
                    };
                    script.onerror = () => reject(new Error('Failed to load Google Maps script'));
                }
            });
        },
        initMap(coords) {
            if (!this.map) {
                this.map = new google.maps.Map(this.$refs.googleMap, {
                    ...this.mapOptions,
                    center: coords,
                });
                this.map.addListener('click', this.addMarker);
                this.fetchAndDisplayPins();
                this.drawPolygons();
            } else {
                this.centerMap(coords.lat, coords.lng);
            }
        },
        addMarker(event) {
            const { lat, lng } = event.latLng.toJSON();
            const marker = new google.maps.Marker({
                position: { lat, lng },
                map: this.map,
                title: "New Pin",
                zIndex: 1000
            });
            this.savePin(lat, lng);
        },
        fetchAndDisplayPins() {
            axios.get('/api/v1/pins/', {
                headers: { 'Authorization': `Token ${this.userToken}` }
            })
                .then(response => {
                    response.data.forEach(pin => {
                        this.addMarkerFromData(pin);
                    });
                })
                .catch(error => console.error('Error fetching pins:', error));
        },
        addMarkerFromData(pin) {
            const marker = new google.maps.Marker({
                position: { lat: pin.latitude, lng: pin.longitude },
                map: this.map,
                title: pin.description || "No Description",
                zIndex: 1000
            });
        },
        savePin(lat, lng) {
            axios.post('/api/v1/save/', {
                latitude: lat,
                longitude: lng
            }, {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${this.userToken}`
                }
            })
                .then(response => {
                    console.log('Pin saved:', response.data);
                })
                .catch(error => {
                    console.error('Error saving pin:', error.response ? error.response.data : error);
                });
        },
        centerMap(lat, lng) {
            this.map.panTo({ lat, lng });
        }
    },
};
</script>

<style>
.google-map {
    width: 100%;
    height: 400px;
}
</style>
