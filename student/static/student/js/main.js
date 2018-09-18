Vue.config.devtools = true;

import Vue from 'vue';
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify);

import CourseList from './components/course-list.vue';
import ElementList from './components/element-list.vue';

export const serverBus = new Vue();

const vm = new Vue({
  el: '#student-home',

  components: { CourseList, ElementList },

  delimiters: ["[[","]]"]
});
