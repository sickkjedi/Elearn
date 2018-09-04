import chapter

<template>
  <div id="course-list" class="col-3 list-group">
    <div class="group-section" v-for="group in groups">
      <v-expansion-panel>
        <v-toolbar color="cyan">
          <v-toolbar-title class="grey--text text--darken-4">{{group.group_name}}</v-toolbar-title>
        </v-toolbar>
        <v-expansion-panel-content v-for="course in group.courses_set">
          <div slot="header">{{course.course_name}}</div>
          <v-card>
            <v-card-text>
              <chapter-list v-bind:course_id="course.id"></chapter-list>
            </v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
      </div>
  </div>

</template>

<script>
  import ChapterList from './chapter-list.vue'
  const axios = require('axios');

  const course_api = "/courses_api/";

  export default {
    name: 'course-list',
    data () {
      return {
        groups: []
      }
    },

    methods: {
      loadGroup: function () {
        axios.get(course_api).then(response => {this.groups = response.data;});
      }
    },

    mounted() {
      this.loadGroup()
    },

    components: { ChapterList }
  }
</script>
