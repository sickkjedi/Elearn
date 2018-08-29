import Vue from 'vue';

const axios = require('axios');

const course_api = "/courses_api/";

const vm = new Vue({
  el: '#student-home',
  data: {
    results: [],
    chapters: []
  },
  methods: {
    showCourse: function (course_id){
      alert(course_id);
    }
  },

  mounted() {
    axios.get(course_api)
    .then(response => {this.results = response.data;})
  },

  delimiters: ["[[","]]"]
});
