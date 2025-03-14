import { createApp } from 'vue';
import WebSocketComponent from './WebSocketComponent.js';

console.log('ciao')

const app = createApp({
  components: {
    WebSocketComponent
  },
  template: `
    <div>
      <h1>Bond WebSocket Client</h1>
      <WebSocketComponent />
    </div>
  `
});

app.mount('#body');
