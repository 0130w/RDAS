<template>
  <div class="mx-auto mt-10">
    <h1 class="text-2xl font-bold mb-4">推荐好友</h1>
    <div
      class="container mx-auto py-8 flex flex-wrap "
      v-if="friends"
    >
      <div
        v-for="friend in friends"
        :key="friend.user_id"
        class="w-full md:w-1/2 lg:w-1/3 px-4 mb-8"
      >
        <FriendCard :friend="friend" />
      </div>
    </div>
  </div>
</template>

<script>
import FriendCard from '@comp/basic/FriendCard.vue';
import Axios from 'axios';
import { getToken } from '@/utils/token';

export default {
  components: {
    FriendCard,
  },
  data() {
    return {
      friends: null,
    };
  },
  mounted() {
    this.fetchFriends();
  },
  methods: {
    async fetchFriends() {
      try {
        const response = await Axios.get('/user/friendRecommend', getToken());
        console.log('Fetched friends:', response.data.data.friends);
        this.friends = response.data.data.friends;
      } catch (error) {
        console.error('Error fetching friends:', error);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
