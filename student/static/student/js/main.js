import Vue from 'vue';

const axios = require('axios');

const course_api = "http://127.0.0.1:8000/courses_api/";

const vm = new Vue({
  el: '#student-home',
  data: {
    results: []
  },

  mounted() {
    axios.get(course_api)
    .then(response => {this.results = response.data; console.log(response.data);})
  },

  delimiters: ["[[","]]"]
});
