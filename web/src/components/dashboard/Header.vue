<template>
  <v-app-bar
    app
    clipped-left
    dense
  >
    <v-app-bar-nav-icon @click.stop="updateDrawer()" />
    <v-toolbar-title>Application</v-toolbar-title>
    <v-spacer></v-spacer>
    <Profile :name=profile.name :image=profile.image></Profile>
  </v-app-bar>
</template>

<script>
import axios from 'axios';
import EventBus from '@/helpers/event-bus';
import Profile from '@/components/dashboard/Profile.vue';

export default {
  name: 'Header',
  components: {
    Profile,
  },
  data: () => ({
    drawer: true,
    profile: {
      image: null,
      name: null,
    },
  }),
  methods: {
    updateDrawer() {
      this.drawer = !this.drawer;
      EventBus.$emit('DRAWER_UPDATE', this.drawer);
    },
  },
  beforeMount() {
    axios.get('/profile').then(({ data }) => {
      this.profile.image = data.image;
      this.profile.name = data.name;
    });
  },
};
</script>
