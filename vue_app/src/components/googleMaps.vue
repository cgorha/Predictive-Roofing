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
            map: null
        };
    },
    watch: {
        zipCode(newVal, oldVal) {
            if (newVal !== oldVal) {
                this.getLatLngFromZipCode(newVal).then(coords => {
                    this.mapOptions.center = coords;
                    if (this.map) {
                        this.centerMap(coords.lat, coords.lng);
                    } else {
                        this.initMap();
                    }
                }).catch(error => console.error('Error getting location from zip code:', error));
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
            });
        }).catch(error => console.error('Google Maps API script not loaded:', error));
    },
    methods: {
        getLatLngFromZipCode(zipCode) {
            const apiKey = ''; // Your API key here
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
        loadGoogleMapsScript() {
            return new Promise((resolve, reject) => {
                const apiKey = ''; // Your API key here
                if (window.google && window.google.maps) {
                    resolve();
                } else {
                    const script = document.createElement('script');
                    script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&callback=initMap`;
                    script.async = true;
                    document.head.appendChild(script);
                    window.initMap = () => {
                        resolve();
                        delete window.initMap;
                    };
                    script.onerror = reject;
                }
            });
        },
        initMap() {
            return new Promise(resolve => {
                this.map = new google.maps.Map(this.$refs.googleMap, {
                    ...this.mapOptions,
                    center: this.mapOptions.center,
                });
                this.map.addListener('click', this.addMarker);
                resolve();
            });
        },
        addMarker(event) {
            const { lat, lng } = event.latLng.toJSON();
            const marker = new google.maps.Marker({
                position: { lat, lng },
                map: this.map,
                title: "New Pin"
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
                title: pin.description || "No Description"
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
