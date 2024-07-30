// backend/routes/menuRoutes.js
const express = require('express');
const { getMenu, addMenuItem, updateMenuItem, deleteMenuItem } = require('../controllers/menuController');
const router = express.Router();

router.get('/api/menu', getMenu);
router.post('/api/menu', addMenuItem);
router.put('/api/menu/:id', updateMenuItem);
router.delete('/api/menu/:id', deleteMenuItem);

module.exports = router;