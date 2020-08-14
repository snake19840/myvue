<template>
  <div>

      <input type="text" v-model="message" placeholder="请输入">
      <button @click="up()">提交</button>
    <hr>
    <p>消息是: {{ message }}</p>

  </div>
</template>

<script>
    export default {
        name: "getTest",
        data(){
          return {
              message:this.$route.params.id,

            }
        },
        methods:{
            up(){

                this.axios.get('/search', {
                    params: {
                        p: this.message,
                    }
                })
                    .then( (response)=> {
                        console.log(response.data);
                        this.message=response.data;
                    })
                    .catch( (error) =>{
                        console.log(error);
                    })
                    .then(function () {
                    });

            },
        },
        computed:{
            // message(){
            //   // return   this.$route.params.id
            //     return 1+3
            // },

        },
    }
</script>

<style scoped>

</style>
