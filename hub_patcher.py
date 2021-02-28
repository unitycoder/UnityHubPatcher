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
    /*  Last updated on 2021-2-28.            */
    /*                                        */
    /*  Tested with:                          */
    /*   - v2.4.2                             */
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
        --main-text-a50: rgba(136, 136, 136, 0.5);
        --text-lighter-1: #aaa;
        --light-bg: #ddd;
        --medium: #585858;
        --medium-lighter-1: #686868;
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
    /* icons */
    md-icon.md-default-theme, md-icon, md-menu-content.md-default-theme md-menu-item md-icon, md-menu-content md-menu-item md-icon{
        color: var(--text-lighter-1);
    }
    project-list-item .action md-icon:hover, project-list-item .action .md-icon-button:hover md-icon{
        color: var(--main-text) !important;
    }
    md-card.md-default-theme, md-card {
        color: var(--text-lighter-1) !important;
        background-color: var(--bg-lighter-2);
    }
    project-list-item{
        border-top: solid 1px var(--bg-lighter-1) !important;
    }
    project-list-item md-select:hover .md-select-icon, md-select.md-default-theme .md-select-icon, md-select .md-select-icon {
        color: var(--medium) !important;
    }
    .md-caption{
        color: var(--main-text) !important;
    }
    .learn-nav-bar .learn-url{
        color: var(--main-text) !important;
    }
    project-list .project-list-row:hover {
        background-color: var(--bg-lighter-1) !important;
    }
    md-select.md-default-theme .md-select-value.md-select-placeholder, md-select .md-select-value.md-select-placeholder {
        color: var(--medium);
    }
    md-select.md-default-theme:not([disabled]):focus .md-select-value, md-select:not([disabled]):focus .md-select-value{
        color: var(--text-lighter-1) !important;
    }
    .project-list-container::-webkit-scrollbar, .card-list-container md-tab-content::-webkit-scrollbar {
        background: var(--bg-lighter-2) !important;
    }
    .install-list::-webkit-scrollbar, .elements-container::-webkit-scrollbar, .learn-page::-webkit-scrollbar{
        background: transparent !important;
    }
    .project-list-container::-webkit-scrollbar-thumb:hover, .card-list-container md-tab-content::-webkit-scrollbar-thumb:hover{
        background-color: var(--medium-lighter-1) !important;
        border-color: var(--bg-lighter-2) !important;
    }
    .install-list::-webkit-scrollbar-thumb:hover, .elements-container::-webkit-scrollbar-thumb:hover, .learn-page::-webkit-scrollbar-thumb:hover {
        background-color: var(--medium-lighter-1) !important;
        border-color: var(--bg-lighter-2) !important;
    }
    .project-list-container::-webkit-scrollbar-thumb, .card-list-container md-tab-content::-webkit-scrollbar-thumb {
        background-color: var(--medium) !important;
        border: 5px solid var(--bg-lighter-2) !important;
    }
    .install-list::-webkit-scrollbar-thumb, .elements-container::-webkit-scrollbar-thumb, .learn-page::-webkit-scrollbar-thumb {
        background-color: var(--medium) !important;
        border: 5px solid var(--body-bg) !important;
    }
    .project-list-container::-webkit-scrollbar-track:hover, .card-list-container md-tab-content::-webkit-scrollbar-track:hover{
        background-color: var(--bg-lighter-3) !important;
    }
    .install-list::-webkit-scrollbar-track:hover, .elements-container::-webkit-scrollbar-track:hover, .learn-page::-webkit-scrollbar-track:hover {
        background-color: transparent !important;
    }
    .project-list-container::-webkit-scrollbar-track, .card-list-container md-tab-content::-webkit-scrollbar-track{
        background: var(--bg-lighter-2) !important;
    }
    .install-list::-webkit-scrollbar-track, .elements-container::-webkit-scrollbar-track, .learn-page::-webkit-scrollbar-track {
        background: transparent !important;
    }
    md-select-menu.md-default-theme md-content, md-select-menu md-content, md-menu-content.md-default-theme, md-menu-content {
        background-color: var(--bg-lighter-5) !important;
    }
    md-select-menu.md-default-theme md-content md-option, md-select-menu md-content md-option, md-menu-content.md-default-theme md-menu-item, md-menu-content md-menu-item {
        color: var(--text-lighter-1);
    }
    .install-badge{
        background-color: var(--badge-gray) !important;
    }
    /* input */
    md-input-container.md-default-theme:not(.md-input-invalid).md-input-has-value label, md-input-container:not(.md-input-invalid).md-input-has-value label {
        color: var(--medium-lighter-1) !important;
    }
    md-input-container.md-default-theme .md-input, md-input-container .md-input{
        color: var(--main-text) !important;
        border-color: var(--black-a30) !important;
    }
    md-input-container.md-default-theme .md-input::placeholder, md-input-container .md-input::placeholder{
        color: var(--medium-lighter-1) !important;
    }
    md-input-container:not(.md-input-focused).md-default-theme .md-placeholder, md-input-container:not(.md-input-focused) .md-placeholder, md-input-container:not(.md-input-focused).md-default-theme label, md-input-container:not(.md-input-focused) label{
        color: var(--main-text) !important;
    }
    /* textarea */
    textarea{
        background-color: var(--bg-lighter-3);
        border:none;
        color: var(--medium-lighter-1);
    }
    /* common */
    md-list.md-default-theme md-list-item.md-2-line .md-list-item-text h3,
    md-list md-list-item.md-2-line .md-list-item-text h3,
    md-list.md-default-theme md-list-item.md-2-line .md-list-item-text h4,
    md-list md-list-item.md-2-line .md-list-item-text h4,
    md-list.md-default-theme md-list-item.md-3-line .md-list-item-text h3,
    md-list md-list-item.md-3-line .md-list-item-text h3,
    md-list.md-default-theme md-list-item.md-3-line .md-list-item-text h4,
    md-list md-list-item.md-3-line .md-list-item-text h4 {
        color: var(--text-lighter-1);
    }
    md-list.md-default-theme md-list-item.md-2-line .md-list-item-text p,
    md-list md-list-item.md-2-line .md-list-item-text p,
    md-list.md-default-theme md-list-item.md-3-line .md-list-item-text p,
    md-list md-list-item.md-3-line .md-list-item-text p {
        color: var(--main-text) !important;
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
    md-nav-bar.md-default-theme .md-button._md-nav-button.md-unselected, md-nav-bar .md-button._md-nav-button.md-unselected{
        color: var(--text-lighter);
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
    /* learn item */
    .learn-page .learn-item{
        background-color: var(--bg-lighter-2) !important;
    }
    /* learn item top */
    .learn-top-container .learn-top-items .learn-top-item .learn-top-item-text .learn-top-item-desc {
        color: var(--main-text) !important;
    }
    /* learn dialog */
    .learn-dialog-scrollable-area .learn-dialog-content .learn-dialog-content-info{
        color: var(--main-text) !important;
    }
    /* community card */
    .community-card md-card-content{
        background-color: var(--bg-lighter-2) !important;
    }
    /* community card desc */
    .community-card md-card-content .community-description{
        color: var(--main-text) !important;
    }
    /* beta badge */
    .beta{
        background-color: var(--bg-lighter-4) !important;
    }
    /* update options */
    .um-update-options .md-button:first-child:enabled{
        background-color: var(--bg-lighter-2) !important;
    }
    /* beta description */
    .beta-description{
        background-color: var(--bg-lighter-3) !important;
    }
    /* caret */
    md-menu-content.md-default-theme .md-menu>.md-button:after, md-menu-content .md-menu>.md-button:after{
        color: var(--main-text) !important;
    }
    /* dialog */
    md-dialog.md-default-theme, md-dialog{
        background-color: var(--bg-lighter-2) !important;
        color: var(--main-text) !important;
    }
    /* stepper */
    .md-stepper-indicator-wrapper{
        background-color: var(--bg-lighter-2) !important;
    }
    .md-stepper-indicator.md-active .md-stepper-title, .md-stepper-indicator.md-completed .md-stepper-title{
        color: var(--main-text) !important;
    }
    .md-steppers-linear .md-stepper-title, .md-steppers-linear .md-stepper-title small:not(.md-stepper-error-message){
        color: var(--main-text-a50) !important;
    }
    .md-steppers-horizontal .md-stepper-indicator:after{
        background-color: var(--bg-lighter-5) !important;
    }
    .md-stepper-indicator:not(.md-active) .md-stepper-number{
        background-color: var(--bg-lighter-5) !important;
        color: var(--main-text);
    }
    /* radio */
    md-radio-button.md-default-theme[disabled], md-radio-button[disabled], md-radio-group.md-default-theme[disabled], md-radio-group[disabled] {
        color: var(--main-text-a50) !important;
    }
    md-radio-button.md-default-theme .md-off, md-radio-button .md-off{
        border-color: var(--main-text) !important;
    }
    md-radio-button.md-default-theme[disabled] .md-container .md-off, md-radio-button[disabled] .md-container .md-off, md-radio-button.md-default-theme[disabled] .md-container .md-on, md-radio-button[disabled] .md-container .md-on, md-radio-group.md-default-theme[disabled] .md-container .md-off, md-radio-group[disabled] .md-container .md-off, md-radio-group.md-default-theme[disabled] .md-container .md-on, md-radio-group[disabled] .md-container .md-on{
        border-color: var(--main-text-a50) !important;
    }
    /* checkbox */
    md-checkbox.md-default-theme:not(.md-checked) .md-icon, md-checkbox:not(.md-checked) .md-icon{
        border-color: var(--main-text) !important;
    }
    /* back button */
    .md-button.md-default-theme.md-accent[disabled], .md-button.md-accent[disabled], .md-button.md-default-theme.md-fab[disabled], .md-button.md-fab[disabled], .md-button.md-default-theme.md-raised[disabled], .md-button.md-raised[disabled], .md-button.md-default-theme.md-warn[disabled], .md-button.md-warn[disabled], .md-button.md-default-theme[disabled], .md-button[disabled]{
        color: var(--main-text-a50) !important;
    }
    /* module table container */
    .module-table-container::-webkit-scrollbar,
    .module-table-container::-webkit-scrollbar-track{
        background: var(--bg-lighter-2) !important;
    }
    .module-table-container::-webkit-scrollbar-thumb{
        background-color: var(--medium) !important;
        border: 5px solid var(--bg-lighter-2) !important;
    }
    .module-table-container::-webkit-scrollbar-thumb:hover{
        background-color: var(--medium-lighter-1) !important;
        border-color: var(--bg-lighter-3) !important;
    }
</style>
"""

if len(sys.argv) == 2:
    path = sys.argv[1]
    os.chdir(os.path.join(path, "resources"))
    print("Extracting app...")
    subprocess.run("npx asar extract app.asar app", shell=True)
    print("Backing up...")
    os.rename("app.asar", "app.asar.bak")
    os.chdir(os.path.join("app", "client", "dist"))
    
    print("Patching...")
    for line in fileinput.FileInput("index.html", inplace=1):
        if "</head>" in line:
            line=line.replace(line,css + line)
        print(line, end="")
    
    print("Done! It's dark now. :D")
