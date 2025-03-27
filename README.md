# @p0llen/wakeword-react

**Status:** 🚧 In Testing  
**License:** MIT

> Free, open-source wake-word detection package using PyTorch, with an associated npm package for React-based integration.  
> Includes CLI tools, real-time microphone access, and GPU-accelerated training capabilities.

---

## 🔧 How It Works

Install the Python backend (`wakeword-detector`) for model training and ONNX export. Then, install this React package for in-browser wakeword detection.

When sound input matches the trained model, the React component will be notified — enabling real-time browser-based wakeword detection.

---

## 🚀 Usage

```jsx
import { useWakeword, WakewordDemo } from "@p0llen/wakeword-react";

function App() {
  return <WakewordDemo />;
}
```

---

## 🔥 Features

- 🎤 Real-time wakeword detection in the browser  
- ⚛️ React component (`useWakeword`) for easy integration  
- 🧠 ONNX model inference with `onnxruntime-web`  
- 🎛️ Adjustable confidence thresholds and visual feedback  
- 🔁 Fully customizable — bring your own wakeword  
- 🧪 Demo UI (`WakewordDemo` component) included for instant testing  

---

## 🖼 Demo Preview

![Wakeword React UI](https://github.com/P0llen/wakeword-detector/blob/main/docs/Wakeword%20React.png?raw=true)

---

## 📦 Installation

### 1. Backend (Python)

Install the backend model trainer and exporter:

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple wakeword-detector
```

### 2. Frontend (React)

```bash
npm install @p0llen/wakeword-react
```

---

## 📋 Requirements

- React 17 or 18+  
- Modern browser (Chrome, Edge, Brave, etc.)  
- ONNX model trained using [`wakeword-detector`](https://test.pypi.org/project/wakeword-detector/)

---

## 🤝 Contributing

Found a bug or want to suggest a feature?  
Open an issue or PR — contributions welcome!