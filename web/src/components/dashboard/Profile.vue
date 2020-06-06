<template>
  <v-menu
    v-model="menu"
    :close-on-content-click="false"
    :nudge-width="200"
    offset-y
  >
    <template v-slot:activator="{ on }">
      <v-btn
        icon
        large
        v-on="on"
        class="mr-1"
      >
        <v-avatar size="32" color="indigo">
          <v-icon v-if="!image" dark>mdi-account-circle</v-icon>
          <img v-else :src="image" :alt="name">
        </v-avatar>
      </v-btn>
    </template>

    <v-card>
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <img :src="image" :alt="name">
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>{{ name }}</v-list-item-title>
            <v-list-item-subtitle>Free account</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list>
        <v-list-item :to="{ name: 'Settings' }">
          <v-list-item-action>
            <v-icon>mdi-settings</v-icon>
          </v-list-item-action>
          <v-list-item-title>Settings</v-list-item-title>
        </v-list-item>
      </v-list>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn text href="/logout">
            <v-icon>mdi-logout</v-icon>
            Logout
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-menu>
</template>

<script>

export default {
  name: 'Profile',
  props: {
    name: String,
    image: String,
  },
  data() {
    return {
      menu: false,
    };
  },
};
</script>
