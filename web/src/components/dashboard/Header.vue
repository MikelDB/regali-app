<template>
  <div class="header">
    <Profile/>
    <Timer/>
  </div>
</template>

<script>
import Profile from '@/components/dashboard/Profile.vue';
import Timer from '@/components/dashboard/Timer.vue';


export default {
  name: 'Header',
  components: {
    Profile,
    Timer,
  },
};
</script>
<style>
.header {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 64px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
</style>
