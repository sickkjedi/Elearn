Vue.config.devtools = true;

import Vue from 'vue';
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify);

import CourseList from './components/course-list.vue';

const vm = new Vue({
  el: '#student-home',

  components: { CourseList },

  delimiters: ["[[","]]"]
});
