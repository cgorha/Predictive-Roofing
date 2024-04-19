<template>
    <div ref="googleMap" class="google-map"></div>
</template>

<script>
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
    },
    data() {
        return {
            map: null
        };
    },
    watch: {
        zipCode: {
            immediate: true,
            handler(newVal, oldVal) {
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
        }
    },
    mounted() {
        this.loadGoogleMapsScript().then(() => {
        }).catch(error => console.error('Google Maps API script not loaded:', error));
    },
    methods: {
        getLatLngFromZipCode(zipCode) {
            return new Promise((resolve, reject) => {
                const apiKey = 'AIzaSyDi2ZmGQl1glP7d1LwVYERsqQl1vt9PMYw';
                const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${zipCode}&key=${apiKey}`;
                console.log(zipCode)

                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        if (data.results && data.results.length > 0) {
                            const { lat, lng } = data.results[0].geometry.location;
                            resolve({ lat, lng });
                        } else {
                            reject('No results found');
                        }
                    })
                    .catch(error => reject(error));
            });
        },
        loadGoogleMapsScript() {
            return new Promise((resolve, reject) => {
                const apiKey = 'AIzaSyDi2ZmGQl1glP7d1LwVYERsqQl1vt9PMYw';
                if (window.google && window.google.maps) {
                    resolve();
                } else {
                    window.resolveGoogleMapsPromise = () => {
                        resolve();
                        delete window.resolveGoogleMapsPromise;
                    };

                    const script = document.createElement('script');
                    script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&callback=resolveGoogleMapsPromise`;
                    script.async = true;
                    document.head.appendChild(script);
                    script.onerror = reject;
                }
            });
        },
        initMap() {
            this.map = new google.maps.Map(this.$refs.googleMap, {
                ...this.mapOptions,
                center: this.mapOptions.center,
            });
            new google.maps.Marker({
                position: this.mapOptions.center,
                map: this.map,
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
