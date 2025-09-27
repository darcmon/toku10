import { createRouter, createWebHistory } from 'vue-router'

import CounterView from '../views/CounterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/counter',
      name: 'Counter',
      component: CounterView,
    },
  ],
})

export default router
