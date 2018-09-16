import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Start from './views/Start.vue'
import Routes from './views/Routes.vue'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: Home
    // },
    {
      path: '/',
      name: 'start',
      component: Start
    },
    {
      path: '/route/:sLat/:sLon/:fLat/:fLon/:s',
      name: 'routes',
      component: Routes
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
