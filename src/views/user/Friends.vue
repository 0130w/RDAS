<template>
  <div class="container mx-auto py-8">
    <!-- 第一行 -->
    <div class="flex flex-wrap -mx-4">
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

export default {
  components: {
    FriendCard,
  },
  data() {
    return {
      friends: [
        {
          avatarUrl: 'https://avatars.githubusercontent.com/u/20411648?v=4',
          name: 'LiuYX',
          user_id: '20411648',
          hobbies: 'Coding, Reading, Writing, Writing, Writing, Writing, Writing, Writing',
          city: 'Shanghai',
          followers: 100,
          comments_written: 1000,
          average_rating: 4.5,
        },
        {
          avatarUrl: 'https://avatars.githubusercontent.com/u/20411648?v=4',
          name: 'LiuYX',
          user_id: '20411648',
          hobbies: 'Coding, Reading, Writing, Writing, Writing, Writing, Writing, Writing',
          city: 'Shanghai',
          followers: 100,
          comments_written: 1000,
          average_rating: 4.5,
        },
        {
          avatarUrl: 'https://avatars.githubusercontent.com/u/20411648?v=4',
          name: 'LiuYX',
          user_id: '20411648',
          hobbies: 'Coding, Reading, Writing, Writing, Writing, Writing, Writing, Writing',
          city: 'Shanghai',
          followers: 100,
          comments_written: 1000,
          average_rating: 4.5,
        },
        {
          avatarUrl: 'https://avatars.githubusercontent.com/u/20411648?v=4',
          name: 'LiuYX',
          user_id: '20411648',
          hobbies: 'Coding, Reading, Writing, Writing, Writing, Writing, Writing, Writing',
          city: 'Shanghai',
          followers: 100,
          comments_written: 1000,
          average_rating: 4.5,
        },
        {
          avatarUrl: 'https://avatars.githubusercontent.com/u/20411648?v=4',
          name: 'LiuYX',
          user_id: '20411648',
          hobbies: 'Coding, Reading, Writing, Writing, Writing, Writing, Writing, Writing',
          city: 'Shanghai',
          followers: 100,
          comments_written: 1000,
          average_rating: 4.5,
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
