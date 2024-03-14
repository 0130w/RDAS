<template>
  <div class="max-w-xl bg-white shadow-md rounded-lg overflow-hidden">
    <div class="flex items-center justify-between px-4 py-3 bg-gray-200">
      <div class="flex items-center">
        <img
          :src="friend.avatarUrl"
          class="h-20 w-20 rounded-full object-cover mr-6"
          :alt="friend.name"
        >
        <div>
          <p class="text-lg font-semibold text-gray-800">{{ friend.name }}</p>
          <p class="text-sm text-gray-600">User ID: {{ friend.user_id }}</p>
          <p class="text-sm text-gray-600">Followers: {{ friend.followers }}</p>
          <p class="text-sm text-gray-600">City: {{ friend.city }}</p>
        </div>
        <button
          @click="addFriend(friend.id)"
          class="bg-blue-500 hover:bg-blue-700 text-sm text-white font-bold py-3 px-4 rounded-full ml-10"
        >
          Add friend
        </button>
      </div>
    </div>
    <div class="px-4 py-3">
      <p class="text-gray-700 text-base">Hobbies: {{ friend.hobbies }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    friend: {
      type: Object,
      required: true,
    },
  },
  methods: {
    addFriend(id) {
      // 发送添加好友的请求...
      console.log(`已发送添加好友请求给ID: ${id}`);
    },
  },
};
</script>

<style>
/* Tailwind CSS classes go here */
</style>
