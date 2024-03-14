<template>
  <div class="max-w-md mx-auto bg-white rounded-xl shadow-md md:max-w-2xl rounded-lg">
    <div class="p-4">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-lg font-semibold text-gray-900">排行榜</h2>
        <div class="text-gray-500 text-sm">更多</div>
      </div>
      <div
        class="space-y-3 overflow-auto"
        style="height: 335px;"
      >
        <div
          v-for="
        (user,
        index)
        in
        users"
          :key="user.id"
          class="flex items-center justify-between"
        >
          <div class="flex items-center">
            <div :class="`bg-${user.color}-500 h-8 w-8 rounded-full flex items-center justify-center text-white`">
              <span>{{ index + 1 }}</span>
            </div>
            <span class="ml-3 text-sm font-medium text-gray-700">{{ user.user_name }}</span>
          </div>
          <div class="text-sm font-semibold text-gray-700 ml-20 mr-4">{{ user.count }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RankingList',
  data() {
    return {
      users: [
        {
          id: 1, user_name: 'Allie', count: 1087, color: 'red',
        },
        {
          id: 2, user_name: 'Bill', count: 1298, color: 'orange',
        },
        {
          id: 3, user_name: 'Boon', count: 1447, color: 'yellow',
        },
        {
          id: 4, user_name: 'Brett', count: 1247, color: 'green',
        },
        {
          id: 5, user_name: 'Brittany', count: 1041, color: 'blue',
        },
        {
          id: 6, user_name: 'Christina', count: 1076, color: 'indigo',
        },
        {
          id: 7, user_name: 'Christopher', count: 1047, color: 'purple',
        },
        {
          id: 8, user_name: 'Danan', count: 1129, color: 'pink',
        },
        {
          id: 9, user_name: 'Dianna', count: 1391, color: 'gray',
        },
        {
          id: 10, user_name: 'Gerald', count: 1682, color: 'green',
        },
        {
          id: 11, user_name: 'Jen', count: 1747, color: 'yellow',
        },
        {
          id: 12, user_name: 'Karen', count: 3048, color: 'blue',
        },
        {
          id: 13, user_name: 'Ken', count: 1396, color: 'red',
        },
        {
          id: 14, user_name: 'Marielle', count: 1840, color: 'orange',
        },
        {
          id: 15, user_name: 'Mark', count: 1308, color: 'yellow',
        },
        {
          id: 16, user_name: 'Michael', count: 1071, color: 'green',
        },
        {
          id: 17, user_name: 'Michelle', count: 1653, color: 'blue',
        },
        {
          id: 18, user_name: 'Rachel', count: 1324, color: 'indigo',
        },
        {
          id: 19, user_name: 'Shannon', count: 1554, color: 'purple',
        },
        {
          id: 20, user_name: 'Steven', count: 1578, color: 'pink',
        },
      ],
    };
  },
};
</script>

  <style scoped>
/* 根据实际需要，可以在这里添加一些额外的CSS样式 */
</style>
