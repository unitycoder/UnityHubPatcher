import subprocess
import os
import sys
import fileinput

css = """<style>
    /******************************************/
    /*                                        */
    /*  HubPatcher and dark theme by Andrew.  */
    /*                                        */
    /******************************************/
    /*                                        */
    /*  Last updated on 2019-07-12.           */
    /*                                        */
    /*  Tested with:                          */
    /*   - v2.0.2-v2.0.4                      */
    /*                                        */
    /******************************************/

    body{
        --body-bg: #111;
        --bg-lighter-1: #141414;
        --bg-lighter-2: #1a1a1a;
        --bg-lighter-3: #1f1f1f;
        --bg-lighter-4: #222;
        --bg-lighter-5: #282828;
        --main-text: #888;
        --text-lighter-1: #aaa;
        --light-bg: #ddd;
        --medium: #585858;
        --medium-ligher-1: #686868;
        --badge-gray: #333;
        --black-a30: rgba(0,0,0,0.3);
    }
    body, md-content{
        background: var(--body-bg) !important;
        color: var(--main-text) !important;
    }
    .unity-top-nav .md-toolbar-tools{
        background-color: var(--light-bg) !important;
        filter: invert(100) !important;
    }
    .unity-side-nav.md-locked-open, .md-locked-open .unity-menu-list{
        background:transparent !important;
        color: var(--text-lighter-1);
    }
    md-icon.md-default-theme, md-icon{
        color: var(--text-lighter-1);
    }
    md-card.md-default-theme, md-card {
        color: var(--text-lighter-1) !important;
        background-color: var(--bg-lighter-2);
    }
    project-list-item{
        border-top: solid 1px var(--bg-lighter-1) !important;
    }
    project-list-item md-select:hover .md-select-icon {
        color: var(--medium) !important;
    }
    .md-caption{
        color: var(--main-text) !important;
    }
    project-list .project-list-row:hover {
        background-color: var(--bg-lighter-1) !important;
    }
    md-select.md-default-theme .md-select-value.md-select-placeholder, md-select .md-select-value.md-select-placeholder {
        color: var(--medium);
    }
    .project-list-container::-webkit-scrollbar, .card-list-container md-tab-content::-webkit-scrollbar {
        background: var(--bg-lighter-2) !important;
    }
    .install-list::-webkit-scrollbar{
        background: transparent !important;
    }
    .project-list-container::-webkit-scrollbar-thumb:hover, .card-list-container md-tab-content::-webkit-scrollbar-thumb:hover{
        background-color: var(--medium-ligher-1) !important;
        border-color: var(--bg-lighter-2) !important;
    }
    .install-list::-webkit-scrollbar-thumb:hover {
        background-color: var(--medium-ligher-1) !important;
        border-color: var(--bg-lighter-2) !important;
    }
    .project-list-container::-webkit-scrollbar-thumb, .card-list-container md-tab-content::-webkit-scrollbar-thumb {
        background-color: var(--medium) !important;
        border: 5px solid var(--bg-lighter-2) !important;
    }
    .install-list::-webkit-scrollbar-thumb {
        background-color: var(--medium) !important;
        border: 5px solid var(--body-bg) !important;
    }
    .project-list-container::-webkit-scrollbar-track:hover, .card-list-container md-tab-content::-webkit-scrollbar-track:hover{
        background-color: var(--bg-lighter-3) !important;
    }
    .install-list::-webkit-scrollbar-track:hover {
        background-color: transparent !important;
    }
    .project-list-container::-webkit-scrollbar-track, .card-list-container md-tab-content::-webkit-scrollbar-track{
        background: var(--bg-lighter-2) !important;
    }
    .install-list::-webkit-scrollbar-track {
        background: transparent !important;
    }
    md-select-menu.md-default-theme md-content, md-select-menu md-content, md-menu-content.md-default-theme, md-menu-content {
        background-color: var(--bg-lighter-5) !important;
    }
    md-select-menu.md-default-theme md-content md-option, md-select-menu md-content md-option, md-menu-content.md-default-theme md-menu-item, md-menu-content md-menu-item {
        color: var(--text-lighter-1);
    }
    .install-badge{
        background-color: var(badge-gray) !important;
    }
    md-input-container.md-default-theme:not(.md-input-invalid).md-input-has-value label, md-input-container:not(.md-input-invalid).md-input-has-value label {
        color: var(--medium-ligher-1) !important;
    }
    md-input-container.md-default-theme .md-input, md-input-container .md-input{
        color: var(--main-text) !important;
        border-color: var(--black-a30) !important;
    }
    md-input-container.md-default-theme .md-input::placeholder, md-input-container .md-input::placeholder{
        color: var(--medium-ligher-1) !important;
    }
    /* button */
    .md-button.md-default-theme.md-raised, .md-button.md-raised {
        color: var(--text-lighter-1);
        background-color: var(--bg-lighter-4);
    }
    .md-button.md-default-theme.md-raised:not([disabled]):hover, .md-button.md-raised:not([disabled]):hover {
        background-color: var(--bg-lighter-5);
    }
    .md-button.md-default-theme.md-raised:not([disabled]).md-focused, .md-button.md-raised:not([disabled]).md-focused {
        background-color: var(--bg-lighter-1);
    }
    /* tabs */
    md-tabs.md-default-theme .md-tab, md-tabs .md-tab {
        color: var(--main-text);
    }
    /* user menu */
    .um-user-account .md-button:first-child:enabled:not(:hover) {
        background-color: transparent !important;
    }
    .um-user-account .md-body-2:not(a) {
        color: var(--main-text) !important;
    }
    .um-user-account md-card{
        background:transparent;
    }
</style>\n"""

if len(sys.argv) == 2:
    path = sys.argv[1]
    os.chdir(os.path.join(path, "resources"))
    print("Extracting app...")
    subprocess.run("npx asar extract app.asar app", shell=True)
    print("Backing up...")
    os.rename("app.asar", "app.asar.bak")
    os.chdir("app\client\dist")
    
    print("Patching...")
    for line in fileinput.FileInput("index.html", inplace=1):
        if "</head>" in line:
            line=line.replace(line,css + line)
        print(line, end="")
    
    print("Done! It's dark now. :D")
