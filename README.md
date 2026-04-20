# Game Creator

A browser-based game development tool that allows you to create, edit, and play games directly in your web browser. Game Creator provides an integrated IDE with a file manager, code editor, asset management, and a real-time game player with 3D rendering and physics simulation.

## Features

### Editor (index.html)
- **Project Management**: Create and manage multiple game projects with metadata and descriptions
- **File System**: Full file tree navigation with support for folders and multiple file types
- **Code Editor**: Integrated code editor with multiple editing modes (Visual, Code)
- **Asset Management**: Upload, organize, and preview game assets with filtering and categorization
- **Live Preview**: Toggle between different editor views (Files, Assets, Code)
- **Terminal/Output Panel**: View compilation output and debugging information
- **Resizable Layouts**: Drag-to-resize panels for customized workspace layouts
- **Project Templates**: Welcome screen with project initialization options

### Player (player.html)
- **3D Rendering**: Canvas-based 3D rendering with support for triangles and tetrahedrons
- **Physics Engine**: Gravity, collision detection, and movement simulation
- **Game Objects**: Dynamic game objects with properties (position, rotation, collision mesh)
- **World System**: Support for multiple worlds/levels with seamless transitions via portals
- **Inventory System**: Item management with equippable slots and tools
- **Interactive Objects**: Pickable items, doors, platforms, portals, vehicles
- **Pause Menu**: In-game menu with save/load functionality
- **Game State Persistence**: Auto-save to browser storage with export/import capabilities
- **Overlay UI**: Real-time object information and selection display

## Getting Started

### Opening the Tool
1. Open `index.html` in a modern web browser
2. Create a new project or select an existing one
3. Use the editor tabs to switch between Files, Assets, and Code views

### Creating a Game
1. Navigate to the **Files** tab to organize your game structure
2. Create game code in the **Code** tab - write your game logic and object definitions
3. Manage game assets in the **Assets** tab (upload images, sprites, textures)
4. Click the **Run** button to launch your game in a new window

### Playing Your Game
1. The game runs in `player.html` with full 3D rendering
2. Use keyboard controls:
   - **Arrow Keys / WASD**: Move player
   - **Space**: Jump
   - **Z-M keys**: Switch equipped inventory slots
   - **Esc**: Pause menu
   - **Click**: Select objects in the world

## Project Structure

```
Game-creator/
├── index.html          # Game Creator IDE/Editor
├── player.html         # Game Player/Runtime
├── README.md           # This file
├── LICENSE             # Project license
├── CODE_OF_CONDUCT.md  # Community guidelines
├── CONTRIBUTING.md     # Contribution guidelines
└── .github/            # GitHub workflows and templates
```

## Core Components

### Editor Features

#### Project Panel
- Display current project name and description
- Project metadata and creation date
- Quick access to project settings

#### File Manager
- Tree-based file browser
- Create, delete, and rename files
- Support for folders and file organization
- File type icons

#### Asset Library
- Asset categorization (Sprites, Textures, Models, Audio, etc.)
- Search and filter functionality
- Drag-and-drop asset management
- Preview panel with asset details
- Download individual assets

#### Code Editor
- Syntax-aware editing
- Multiple file editing
- Mode switching (Visual/Code modes)
- Integrated user code section with template functions

### Game Engine Features

#### GameObject System
- Base `GameObject` class for all entities
- `WorldObject` for physical world elements
- Specialized classes: `Tree`, `Ladder`, `Platform`, `Portal`, `Door`, `Car`
- Support for custom properties (position, rotation, collision meshes)

#### Physics System
- Gravity and falling mechanics
- Collision detection (sphere-triangle and sphere-tetrahedron)
- Player movement and jumping
- Surface interaction detection

#### Inventory System
- Item management with quantities
- Equippable slots (7 slots via Z-M keys)
- Tool-based items with commands
- Item pickup and drop mechanics

#### World/Portal System
- Multiple world support (world 0, world 1, etc.)
- Portal objects for world transitions
- Object visibility per world

#### Rendering
- 3D isometric-style perspective
- Texture support for objects
- Grid overlay
- Dynamic object coloring
- Camera system with focal point tracking

## Usage Examples

### Creating a Simple Game

1. **Define your player** in the code:
```javascript
let objects = [
    {
        id: 'player',
        name: 'Player',
        x: 0, y: 0, z: 0,
        isplayer: true,
        // triangle and collision mesh definitions...
    }
];
```

2. **Add world objects** (trees, platforms, etc.):
```javascript
// Objects automatically spawned via class instantiation
new Tree({x: 100, y: 0, z: 50});
new Platform({x: 200, y: 0, z: 100, width: 100, height: 20, depth: 50});
```

3. **Define game mechanics** in custom code sections:
```javascript
function initUser() {
    // Setup code
}

function loopUser() {
    // Per-frame game logic
}
```

4. **Run** and test your game

## Browser Support
Game Creator requires a modern browser with support for:
- Canvas 2D API
- ES6 JavaScript
- LocalStorage (for save data)
- File API (for asset uploads)

Recommended: Chrome, Firefox, Safari, or Edge (latest versions)

## File Format

### Save/Load System
- Game state auto-saves to browser LocalStorage
- Manual export as JSON with full game state
- Import backup files to restore previous sessions
- Save includes: inventory, object positions, world state, progress

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **Arrow Keys / WASD** | Move |
| **Space** | Jump |
| **Esc** | Toggle Pause Menu |
| **Z-M** | Switch Inventory Slots |
| **P** | Toggle Drive Overlay (in vehicles) |
| **Click** | Select/Interact with Objects |
| **I** / **O** / **K** | Vehicle Controls (Accelerate/Reverse/Brake) |
| **J / L** | Vehicle Steering |

## Architecture

### Client-Side Only
- No server required - runs entirely in the browser
- All data stored in localStorage or exported as JSON
- Games are self-contained HTML/JavaScript bundles
- Asset embedding via data URLs

### Two-File System
- **index.html**: Game creator IDE with project and asset management
- **player.html**: Game runtime and 3D engine
- Games compile to standalone player instances

## Known Limitations

- Single-player focused (multiplayer not implemented)
- Limited to browser performance for physics simulation
- Assets must be compatible with Canvas rendering
- Maximum local storage size dependent on browser (~5-50MB)
- 3D rendering uses 2D canvas isometric projection (not WebGL)

## Future Enhancement Ideas

Here are some improvements that could enhance the project:

1. **Module Structure**: Split large HTML files into separate JavaScript modules
2. **Build System**: Add a build process to minify and optimize for production
3. **Script API Documentation**: Create detailed docs for the game script interface
4. **Pre-built Templates**: Offer more game templates (Platformer, RPG, Puzzle, etc.)
5. **Multiplayer Support**: WebSocket integration for collaborative play
6. **Audio System**: Sound effects and music support
7. **Mobile Controls**: Touch/accelerometer input for mobile devices
8. **Shader Support**: WebGL backend for advanced graphics
9. **Debugging Tools**: Built-in debugger and profiler
10. **Version Control**: Track project history with undo/redo
11. **Collaborative Editing**: Real-time multi-user editing
12. **Asset Store**: Pre-made asset library and monetization
13. **Export Options**: Generate standalone game files
14. **Networking**: Save projects to cloud storage

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to Game Creator.

## License

This project is licensed under the terms specified in [LICENSE](LICENSE).

## Code of Conduct

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to understand the community standards and expectations.

## Support

For questions, bug reports, or feature requests, please open an issue on GitHub.

---

**Happy game creating! 🎮**