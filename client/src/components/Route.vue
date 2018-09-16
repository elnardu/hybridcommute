<template>
  <div class="row py-2 border-bottom">
    <div class="col p-3">
      <h2>Step {{num+1}}</h2>
      <p>
        From: {{data.legs[0].start_address}}
        <br/>
        To:   {{data.legs[0].end_address}}
        <br/>
        Travel by: {{data.legs[0].steps[1] ? data.legs[0].steps[1].travel_mode : data.legs[0].steps[0].travel_mode}}
      </p>
    </div>
    <div class="col">
      <GmapMap
          :center="center"
          :zoom="13"
          map-type-id="terrain"
          style="width: 100%; height: calc(30vh)">
          <GmapPolyline
            :path="polyline"
            :options="{strokeColor: '#3498db'}"
          />
      </GmapMap>
    </div>
  </div>
</template>

<script>
import {gmapApi} from 'vue2-google-maps'
export default {
  name: 'Route',
  props: ['data', 'num'],
  data() {
    return {
      polyline: []
    }
  },
  mounted() {
    console.log(gmapApi())
    setTimeout(() => {
      this.polyline = gmapApi().maps.geometry.encoding.decodePath(this.data.overview_polyline.points)
    }, 2000)
  },
  computed: {
    center() {
      let bounds = this.data.bounds
      return {
        "lat": (bounds.northeast.lat + bounds.southwest.lat) / 2,
        "lng": (bounds.northeast.lng + bounds.southwest.lng) / 2 
      }
    }
  }
}
</script>

<style scoped>
</style>