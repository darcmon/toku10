import { createRouter, createWebHistory } from 'vue-router'

import BoxscoreView from '../views/BoxscoreView.vue'
import CounterView from '../views/CounterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/games/1',
    },
    {
      path: '/games/:gameId',
      name: 'Boxscore',
      component: BoxscoreView,
    },
    {
      path: '/counter',
      name: 'Counter',
      component: CounterView,
    },
  ],
})

export default router
