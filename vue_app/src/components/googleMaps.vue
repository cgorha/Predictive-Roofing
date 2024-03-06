<template>
    <div ref="googleMap" class="google-map"></div>
</template>

<script>
export default {
    name: 'GoogleMapsComponent',
    mounted() {
        this.loadGoogleMapsScript().then(() => {
            this.initMap();
        }).catch(error => console.error('Google Maps API script not loaded:', error));
    },
    props: {
        mapOptions: {
            type: Object,
            default: () => ({}),
        },
    },
    methods: {
        loadGoogleMapsScript() {
            return new Promise((resolve, reject) => {
                if (window.google && window.google.maps) {
                    resolve(); // Script is already loaded
                } else {
                    // Define the global callback first
                    window.resolveGoogleMapsPromise = () => {
                        resolve();
                        // Cleanup
                        delete window.resolveGoogleMapsPromise;
                    };

                    const script = document.createElement('script');
                    script.src = `https://maps.googleapis.com/maps/api/js?key=&callback=resolveGoogleMapsPromise`;
                    script.async = true;
                    document.head.appendChild(script);
                    script.onerror = reject;
                }
            });
        },
        initMap() {
            const map = new google.maps.Map(this.$refs.googleMap, this.mapOptions);

        },
    },
};
</script>

<style>
.google-map {
    width: 100%;
    height: 400px; /* Adjust as needed */
}
</style>