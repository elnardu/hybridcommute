<template>
  <div class="container-fluid">
    <div v-if="!loaded" class="row justify-content-center">
      <h1>Loading...</h1>
    </div>
    <Route v-if="loaded" v-for="(r, i) in routes" :data="r[0]" :key="i" :num="i"/>
  </div>
</template>

<script>
import axios from "axios"
import Route from '@/components/Route.vue'

export default {
  name: "Routes",
  components: {
    Route
  },
  data() {
    return {
      routes: [],
      loaded: false
    };
  },
  mounted() {
    this.getRoutes()
  },
  methods: {
    getRoutes() {
      this.loaded = false;
      axios.post(this.$store.state.apiUrl + "/api/calc", {
        to: {
          lat: this.$route.params.sLat,
          lon: this.$route.params.sLon
        },
        from: {
          lat: this.$route.params.fLat,
          lon: this.$route.params.fLon
        },
        reversed: this.$route.params.s
      }).then((data) => {
        console.log(data)
        this.routes = data.data[2]
        this.loaded = true
      })
    }
  },
  watch: {
    '$route'() {
      this.getRoutes()
    }
  }
}
</script>

<style scoped>
</style>