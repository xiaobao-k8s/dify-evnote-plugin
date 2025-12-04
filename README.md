## evnote

# Evernote Management Plugin

## Overview

The **Evernote Management Plugin** provides seamless integration between Dify and Evernote, allowing users to easily manage notes and notebooks within workflows. This plugin supports core functionalities such as retrieving notebook lists and creating new notes, helping users efficiently manage knowledge content in automated workflows.

## Tool List

This plugin includes the following tools:

1. **Get Notebook List**: Retrieves all notebooks from the user's Evernote account
2. **Create Note**: Creates a new note in a specified notebook or the default notebook

## Configuration

1. **Install the Plugin**
   - Navigate to the Dify App Market
   - Search for "Evernote Management"
   - Click "Install" to add the plugin to your workspace

2. **Configure Authentication**
   - Open plugin settings
   - Enter your Evernote Developer Token
   - Set sandbox mode (enabled by default for testing)
   - Set region (defaults to domestic site app.yinxiang.com)
   - Save configuration

   > **Obtain Developer Token**:
   > - Chinese users: Visit https://app.yinxiang.com/api/DeveloperToken.action
   > - International users: Visit https://www.evernote.com/api/DeveloperToken.action

## Usage Guide

### Get Notebook List

**Function**: Retrieves all notebooks from the user's Evernote account

**Parameters**: None

**Return Result**: A JSON array containing all notebook information, each notebook includes the following fields:
- `guid`: Unique notebook identifier
- `name`: Notebook name
- `defaultBook`: Whether it's the default notebook

### Create Note

**Function**: Creates a new note in a specified notebook or the default notebook

**Parameters**:
- `title`: Note title (required)
- `content`: Note content (required)
- `book_name`: Notebook name (optional, uses default notebook if not specified)

**Return Result**: A JSON object containing the GUID of the newly created note

## Example Workflows

### Example 1: View All Notebooks

1. Add the "Get Notebook List" tool to your Dify workflow
2. Configure authentication information
3. Run the workflow
4. View the returned notebook list

### Example 2: Create a New Note

1. Add the "Create Note" tool to your Dify workflow
2. Configure authentication information
3. Enter parameters:
   - `title`: "New Project Plan"
   - `content`: "This is a detailed project plan containing all tasks and goals for Q1."
   - `book_name`: "Work Notes"
4. Run the workflow
5. Retrieve the GUID of the newly created note

## Notes

1. **Developer Token Security**: Please keep your developer token secure and do not share it publicly
2. **Sandbox Mode**: Use sandbox mode for testing to ensure functionality before switching to production mode
3. **Region Settings**: Chinese users should keep the default domestic site setting, international users should set it to False
4. **API Version**: The plugin automatically checks API version compatibility to ensure proper communication with Evernote services

## Frequently Asked Questions

**Issue**: Failed to retrieve notebook list
**Solution**: Check if your developer token is valid and your network connection is normal

**Issue**: Failed to create note
**Solution**: Ensure the title and content are not empty, and that the specified notebook name exists

## Update Log

### Version 0.0.1
- Initial release
- Support for retrieving notebook list functionality
- Support for creating notes functionality
- Support for sandbox mode and region settings

## Development Guide

### Installation

To set up the plugin for local development:

```bash
# Install dependencies
pip install -r requirements.txt
```
### Remote Debugging

To debug the plugin remotely with Dify:

1. **Get Debugging Credentials**
   - Go to the "Plugin Management" page in Dify
   - Retrieve the remote server address and debug key

2. **Configure Environment Variables**
   - Copy `.env.example` to create a new `.env` file:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and fill in the debugging credentials:
     ```
     INSTALL_METHOD=remote
     REMOTE_INSTALL_URL=debug.dify.ai:5003
     REMOTE_INSTALL_KEY=********-****-****-****-************
     ```

3. **Start Debug Server**
   - Run the plugin with the debug configuration:
     ```bash
     python -m main
     ```

4. **Access the Plugin**
   - The plugin will be installed to your Dify workspace automatically
   - Team members can also access the plugin for collaborative testing

### Plugin Packaging

To package the plugin for deployment:

```bash
# Package the plugin
dify plugin package ./evnote2  
```



