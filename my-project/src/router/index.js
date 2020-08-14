import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import getTest from  '@/components/getTest'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    // {
    //   path: '/getTest',
    //   name: 'getTest',
    //   component: getTest
    // },
    {
      path:'/',
      name: 'HelloWorld',
      component:()=>import('@/views/myviews/HelloWorld.vue'),
    },
    {
      path:'/getTest',
      name: 'getTest',
      component:()=>import('@/views/myviews/getTest.vue'),
    },


  ]
})
