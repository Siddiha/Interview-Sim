import express from 'express';
import { createServer } from 'http';
import { Server } from 'socket.io';
import { setupRoutes } from './routes';

const app = express();
const server = createServer(app);
const io = new Server(server);

app.use(express.json());
app.use(express.static('public'));

setupRoutes(app, io);

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});