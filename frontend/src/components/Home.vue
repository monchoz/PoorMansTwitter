<template>
  <div>
    <h1 class="title">Poor Man's Twitter</h1>
    <form>
      <h2 class="subtitle">Add your Tweet</h2>
      <div class="field">
        <label class="label">Name</label>
        <div class="control">
          <input v-model="name" class="input" type="text" required>
        </div>
      </div>
      <div class="field">
        <label class="label">Message</label>
        <div class="control">
          <input v-model="message" class="message" maxlength="50" required>
        </div>
      </div>
      <button class="submit" @click="addTweet()">Send</button>
    </form>
    <div class="tweets">
      <div class="tweet" v-for="tweet in tweets">
        <span class="tweet__name">{{ tweet.name }}</span>
        <span class="tweet__message">{{ tweet.message }}</span>
        <span class="tweet__datetime">{{ new Date(tweet.datetime).toLocaleString() }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data () {
    return {
      tweets: [],
      name: '',
      message: ''
    }
  },
  mounted() {
    this.getTweets()
  },
  methods: {
    getTweets() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/tweets/'
      }).then(response => this.tweets = response.data)
    },
    addTweet() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/tweets/',
        data: {
          name: this.name,
          message: this.message
        }
      }).then((response) => {
        this.getTweets()
        this.name = '';
        this.message = '';
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
form {
  max-width: 400px;
  width: 100%;
  margin: 0 auto;
  position: relative;
  background: #F9F9F9;
  padding: 35px;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
input,
textarea {
  width: 100%;
  border: 1px solid #ccc;
  background: #FFF;
  margin: 0 0 5px;
  padding: 10px;
}
label {
  display: block;
  text-align: left;
}
button {
  cursor: pointer;
  width: 100%;
  border: none;
  background: #4CAF50;
  color: #FFF;
  padding: 10px;
  font-size: 15px;
}
.control {
  border: medium none !important;
  margin: 0 0 10px;
  min-width: 95%;
  padding: 0;
  width: 95%;
}
.tweets {
  display: flex;
  flex-wrap: wrap;
}
.tweet {
  display: flex;
  flex-direction: column;
  width: 20%;
  background: #fff;
  margin: 0 auto;
  margin-top: 50px;
  border-radius:3px;
  padding: 30px;
  border-bottom: 1px solid #e6ecf0;
  border-top: 1px solid #e6ecf0;
  text-align: left;
}
.tweet__name {
  font-weight: bold;
}
.tweet__datetime {
  color: #657786;
  font-weight: normal;
}
.tweet__message {
  margin: 10px 0px;
}
</style>
