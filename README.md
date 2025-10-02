# Tailspin Toys

This repository contains the project for a 1 hour guided workshop to explore GitHub Copilot Agent Mode and related features in Visual Studio Code. The project is a website for a fictional game crowd-funding company, with a [Flask](https://flask.palletsprojects.com/en/stable/) backend using [SQLAlchemy](https://www.sqlalchemy.org/) and [Astro](https://astro.build/) frontend using [Svelte](https://svelte.dev/) for dynamic pages.

To begin the workshop, start at [docs/README.md](./docs/README.md)

Or, if just want to run the app...

## Launch the site

A script file has been created to launch the site. You can run it by:

```bash
./scripts/start-app.sh
```

Then navigate to the [website](http://localhost:4321) to see the site!

## MCP Demo Site

This repository includes an MCP (Model Context Protocol) demo website that showcases how to build an enterprise-ready MCP registry using Azure API Center.

### Accessing the MCP Demo

Once the application is running, you can access the MCP demo at:
- **Main page**: [http://localhost:4321/mcp](http://localhost:4321/mcp)
- **About page**: [http://localhost:4321/mcp/about](http://localhost:4321/mcp/about)
- **Onboard page**: [http://localhost:4321/mcp/onboard](http://localhost:4321/mcp/onboard)

### MCP Demo Features

- **Search functionality**: Search for MCP servers by name or description
- **Advanced filtering**: Filter by Type (Local/Remote), Vendor (Microsoft/Partner), and Endpoint
- **Sorting options**: Sort servers by name or vendor
- **View modes**: Switch between grid and list views
- **Responsive design**: Modern, clean UI with dark mode support
- **Mock data**: Includes sample MCP servers for demonstration purposes

## License 

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) for the full terms.

## Maintainers 

You can find the list of maintainers in [CODEOWNERS](./.github/CODEOWNERS).

## Support

This project is provided as-is, and may be updated over time. If you have questions, please open an issue.
