import { defineComponent, ref, onMounted, onUnmounted } from 'vue';

export default defineComponent({
  name: 'WebSocketComponent',

  setup() {
    const messages = ref([]);
    const connectionStatus = ref('disconnected');
    const messageInput = ref('');
    let socket = null;

    // Determine WebSocket URL based on current page location
    const getWebSocketUrl = () => {
      const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const host = window.location.hostname;
      const port = window.location.port || (protocol === 'wss:' ? '443' : '80');
      // Assuming the backend is at the same host but on port 8000
      return `${protocol}//${host}:8000/ws`;
    };

    const connectWebSocket = () => {
        console.log('hi there', getWebSocketUrl())
      socket = new WebSocket(getWebSocketUrl());

      socket.onopen = () => {
        connectionStatus.value = 'connected';
        addMessage('Connected to server', 'system');
        // Send initial message on connection
        socket.send('Hello from Bond frontend!');
      };

      socket.onmessage = (event) => {
        addMessage(event.data, 'received');
      };

      socket.onclose = () => {
        connectionStatus.value = 'disconnected';
        addMessage('Disconnected from server', 'system');
        // Try to reconnect after a delay
        setTimeout(connectWebSocket, 5000);
      };

      socket.onerror = (error) => {
        addMessage(`WebSocket error: ${error.message}`, 'error');
      };
    };

    const addMessage = (content, type) => {
      messages.value.push({
        id: Date.now() + Math.random(),
        content,
        type,
        timestamp: new Date().toLocaleTimeString()
      });
    };

    const sendMessage = () => {
      if (messageInput.value.trim() && socket && socket.readyState === WebSocket.OPEN) {
        socket.send(messageInput.value);
        addMessage(messageInput.value, 'sent');
        messageInput.value = '';
      }
    };

    onMounted(() => {
      connectWebSocket();
    });

    onUnmounted(() => {
      if (socket) {
        socket.close();
      }
    });

    return {
      messages,
      connectionStatus,
      messageInput,
      sendMessage
    };
  },

  template: `
    <div>
      <div class="connection-status" :class="connectionStatus">
        {{ connectionStatus === 'connected' ? 'Connected' : 'Disconnected' }}
      </div>

      <div>
        <input
          v-model="messageInput"
          @keyup.enter="sendMessage"
          placeholder="Type a message..."
          :disabled="connectionStatus !== 'connected'"
        />
        <button @click="sendMessage" :disabled="connectionStatus !== 'connected'">Send</button>
      </div>

      <div class="messages">
        <div v-for="message in messages" :key="message.id" class="message" :class="message.type">
          <span class="timestamp">[{{ message.timestamp }}]</span>
          <span>{{ message.content }}</span>
        </div>
      </div>
    </div>
  `
});
