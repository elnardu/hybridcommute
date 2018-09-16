<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col">
                <h3>From</h3>
                <GmapMap
                    :center="{lng:-71.0986966, lat:42.3585646}"
                    :zoom="13"
                    map-type-id="terrain"
                    style="width: 100%; height: calc(60vh)"
                    >
                    <GmapMarker
                        :position="from.position"
                        :clickable="true"
                        :draggable="true"
                        @dragend="fromMarkerDrag"
                    />
                </GmapMap>
            </div>
            <div class="col">
                <h3>To</h3>
                <GmapMap
                    :center="{lng:-71.0986966, lat:42.3585646}"
                    :zoom="13"
                    map-type-id="terrain"
                    style="width: 100%; height: calc(60vh)"
                    >
                    <GmapMarker
                        :position="to.position"
                        :clickable="true"
                        :draggable="true"
                        @dragend="toMarkerDrag"
                    />
                </GmapMap>
            </div>
        </div>
        <div class="row justify-content-center mt-3">
          <select class="custom-select mr-2 w-25" v-model="select">
            <option selected value="0">Driving, transit, walking</option>
            <option value="1">Walking, transit, driving</option>
          </select>
          <button class="btn btn-outline-primary" @click="go">Go on a trip</button>
        </div>

    </div>
</template>

<script>
export default {
  name: "Start",
  data() {
    return {
      select: 0,
      from: {
        position: {
          lng: -71.0986966,
          lat: 42.3585646
        }
      },
      to: {
        position: {
          lng: -71.0986966,
          lat: 42.3585646
        }
      }
    }
  },
  methods: {
    fromMarkerDrag(e) {
      this.from.position.lat = e.latLng.lat()
      this.from.position.lng = e.latLng.lng()
    },
    toMarkerDrag(e) {
      this.to.position.lat = e.latLng.lat()
      this.to.position.lng = e.latLng.lng()
    },
    go() {
      this.$router.push({
        name: "routes",
        params: { 
          sLat: this.from.position.lat,
          sLon: this.from.position.lng,
          fLat: this.to.position.lat,
          fLon: this.to.position.lng,
          s: this.select
        }
      })
    }
  }
}
</script>

<style scoped>
</style>