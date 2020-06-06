<template>
  <v-app id="inspire">
    <Navigation></Navigation>
    <Header></Header>
    <Content></Content>
    <Footer></Footer>
  </v-app>
</template>

<script>

import Header from '@/components/dashboard/Header.vue';
import Navigation from '@/components/dashboard/Navigation.vue';
import Content from '@/components/dashboard/Content.vue';
import Footer from '@/components/dashboard/Footer.vue';

export default {
  props: {
    source: String,
  },
  components: {
    Header,
    Navigation,
    Footer,
    Content,
  },
  created() {
    this.$vuetify.theme.dark = true;
  },
};
</script>
