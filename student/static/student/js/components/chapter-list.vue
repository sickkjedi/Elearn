<template>
  <v-list>
    <v-list-tile v-for="chapter in chapters" v-on:click="sendData(chapter.id)">
      <v-list-tile-content>
        <v-list-tile-title v-text="chapter.name"></v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>
  </v-list>
</template>

<script>
  const axios = require('axios');
  import { serverBus } from '../main';

  const course_info_api = "/chapters_api/";

  export default {
    name: "chapter-list",

    props: ['course_id'],

    data () {
      return {
        chapters: []
      }
    },

    methods: {
      loadChapters: function (course_id) {
        axios.get(course_info_api + course_id).then(response => {this.chapters = response.data;});
      },
      sendData: function (chapter_id) {
        serverBus.$emit('sendData', chapter_id)
      }

    },

    mounted() {
      this.loadChapters(this.$props.course_id)
    }

  }
</script>

