<template>
<div id="element-list" class="list-group">
    <div class="element-section" v-for="element in elements">
      <v-expansion-panel popout  color="teal">
        <v-expansion-panel-content>
          <div slot="header">{{element.name}}</div>
          <v-card color="teal">
            <v-card-text>
              <element-data v-bind:element_id="element.id"></element-data>
            </v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
      </div>
  </div>
</template>

<script>
  import ElementData from './element-data.vue'
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
    },

    components: {ElementData}
  }
</script>

