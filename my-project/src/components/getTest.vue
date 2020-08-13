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
              message:'',
            }
        },
        methods:{
            up(){

                this.axios.get('search', {
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
        }
    }
</script>

<style scoped>

</style>
