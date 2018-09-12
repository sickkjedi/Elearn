<template>
  <div>
    <p>{{element[0].description}}</p>
    <div v-if="element[0].te_type == 'HTML'">
      <p>{{element[0].html}}</p>
    </div>
    <div v-else-if="element[0].te_type == 'Reflection'">
      <p>{{element[0].question}}</p>
    </div>
  </div>
</template>

<script>
  const axios = require('axios');

  const element_data_api = "/tei_api/";

  export default {
    name: "element-data",

    props: ['element_id'],

    data () {
      return {
        element: Object
      }
    },

    methods: {
      loadElement: function (element_id) {
        axios.get(element_data_api + element_id).then(response => {this.element = response.data;});
      },
    },

    mounted() {
      this.loadElement(this.$props.element_id)
    }
  }
</script>