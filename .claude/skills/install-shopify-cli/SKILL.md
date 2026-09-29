---
name: install-shopify-cli
description: Install the Shopify CLI globally via npm. Use when the user asks to install, set up, or update the Shopify CLI, or when a `shopify` command is not found.
---

# Install Shopify CLI

1. Install globally:
   ```bash
   npm install -g @shopify/cli@latest
   ```
   Use a long timeout (up to 5 min).
2. Verify:
   ```bash
   shopify version
   ```
3. Report the installed version in one line.

Notes:
- In cloud sessions the install is ephemeral (lost when the container is reclaimed).
- Ignore npm "new major version" notices.
