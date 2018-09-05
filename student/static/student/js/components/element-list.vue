<template>
  <ul>
    <li v-for="element in elements">{{element.name}}</li>
  </ul>
</template>

<script>
  const axios = require('axios');
  import { serverBus } from '../main';

  const course_info_api = "/elements_api/";

  export default {
    name: "element-list",

    data () {
      return {
        elements: []
      }
    },

    methods: {
      loadElements: function (chapter_id) {
        axios.get(course_info_api + chapter_id).then(response => {this.elements = response.data;});
      },
    },

    created() {
      serverBus.$on('sendData', (chapter_id) => {this.loadElements(chapter_id);});
    }
  }
</script>

