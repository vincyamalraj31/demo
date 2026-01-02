# 🐧 Cute Penguin 3D Viewer

A professional-grade interactive 3D model viewer with 360° turntable animation, perfect for showcasing your AI-generated penguin models!

## ✨ Features

### 🎮 Interactive Controls
- **Auto-Rotation**: Smooth 360° turntable animation
- **Manual Control**: Drag to rotate, scroll to zoom
- **Pause/Resume**: Toggle automatic rotation
- **Reset View**: Return to default camera position
- **Wireframe Mode**: Toggle between solid and wireframe rendering

### ⚙️ Advanced Controls
- **Rotation Speed**: Adjust from 0x to 5x speed
- **Light Intensity**: Control studio lighting brightness (0-3)
- **Zoom Control**: Adjust camera distance (2-10 units)
- **Background Colors**: Choose from 6 preset backgrounds
- **Animation Presets**:
  - 🐌 Slow - Gentle rotation
  - ⚡ Normal - Standard speed
  - 🚀 Fast - Quick rotation
  - 🎾 Bounce - Back-and-forth animation

### 📸 Export & Display
- **Screenshot**: Capture high-quality PNG images
- **Fullscreen Mode**: Immersive viewing experience
- **Model Statistics**: Real-time vertex and triangle count

## 🚀 Quick Start

### Option 1: Simple File Open
Just double-click `index.html` to open in your browser!

### Option 2: Local Server (Recommended)
For the best experience with a clean URL:

```bash
# Using Python (recommended)
python server.py
```

Then open: **http://localhost:8000**

### Option 3: Alternative Servers

**Using Python's built-in server:**
```bash
python -m http.server 8000
```

**Using Node.js (if installed):**
```bash
npx http-server -p 8000
```

## 🐧 Adding Your Custom Penguin Model

1. **Generate your 3D model** using AI tools:
   - [Meshy.ai](https://www.meshy.ai) - Text to 3D
   - [Tripo3D](https://www.tripo3d.ai) - Image/Text to 3D
   - [Luma AI Genie](https://lumalabs.ai/genie) - Text to 3D

2. **Download** the model as `.glb` or `.gltf` format

3. **Rename** the file to `penguin.glb`

4. **Place** it in the same folder as `index.html`

5. **Refresh** the page - your penguin will appear!

## 🎨 Customization

### Changing Default Settings
Edit the JavaScript variables in `index.html`:

```javascript
let rotationSpeed = 0.01;  // Rotation speed
camera.position.set(0, 1.5, 5);  // Camera position
keyLight.intensity = 1.2;  // Light intensity
```

### Adding More Backgrounds
Add options to the background selector:

```html
<option value="#yourcolor">Your Color Name</option>
```

## 📋 Keyboard Shortcuts

- **Space**: Pause/Resume rotation
- **R**: Reset view
- **F**: Toggle fullscreen
- **S**: Take screenshot

## 🛠️ Technical Details

- **Renderer**: Three.js (WebGL)
- **Lighting**: Professional 3-point studio setup
- **Shadows**: PCF soft shadows
- **Performance**: 30-60 FPS smooth animation
- **Compatibility**: All modern browsers

## 📦 File Structure

```
penguin-3d-viewer/
├── index.html          # Main viewer application
├── server.py           # Python HTTP server
├── README.md           # This file
└── penguin.glb         # Your 3D model (add this)
```

## 🎯 Use Cases

- Preview AI-generated 3D models
- Create product showcase animations
- Generate marketing materials
- Test 3D model quality
- Create turntable videos for portfolios

## 📸 Creating Turntable Videos

1. Click **Fullscreen** button
2. Start **Screen Recording** (Windows: Win+G, Mac: Cmd+Shift+5)
3. Let the model rotate 360°
4. Stop recording and save as MP4/GIF

## 🤝 Credits

Built with:
- [Three.js](https://threejs.org/) - 3D rendering library
- Inspired by professional animation studio workflows

## 📄 License

Free to use for personal and commercial projects!

---

**Enjoy your 3D penguin viewer! 🐧✨**
