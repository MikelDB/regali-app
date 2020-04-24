<template>
  <div class="dashboard">
    <Header/>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/dashboard/Header.vue';

export default {
  name: 'Dashboard',
  components: {
    Header,
  },
};
</script>
