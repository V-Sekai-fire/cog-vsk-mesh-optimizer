## cog-meshoptimizer

`cog-meshoptimizer` is a tool to optimize 3D assets for efficient rendering and transmission. It uses various algorithms to reduce the size and complexity of 3D models while preserving visual quality.

### Features

- Mesh simplification
- Vertex cache optimization
- Overdraw optimization
- Vertex quantization

### Usage

To optimize a 3D model, use the `cog predict` command with the appropriate input file:

```bash
cog predict -i model_file=@slavic_girl_brown_hair.glb
```

## Example OpenAPI Line Usage

```bash
cog serve
# Ensure the server is running and note the port it is using (it may vary)
curl -o openapi.json http://localhost:<port>/openapi.json
# Open the openapi.json file in https://mermade.github.io/openapi-gui/
# Use the OpenAPI GUI to upload the image
# "model_file": "slavic_girl_brown_hair.glb"
```

### Troubleshooting

If you cannot `cog push` in Docker Desktop, try disabling containerd.
