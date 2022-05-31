import subprocess
import os
import sys
import fileinput

css = """<style id="light">
    /******************************************/
    /*                                        */
    /*  HubPatcher and theme(s) by Andrew.    */
    /*                                        */
    /******************************************/
    /*                                        */
    /*  Last updated on 2022-5-30.            */
    /*                                        */
    /*  Tested with:                          */
    /*   - v3.1.2                             */
    /*                                        */
    /******************************************/

    body {
        --body-bg: #f0f0f0;
        --bg-alt-1: #e0e0e0;
        --bg-alt-2: #d0d0d0;
        --bg-alt-3: #c8c8c8;
        --bg-alt-4: #c0c0c0;
        --bg-alt-5: #b8b8b8;
        --main-text: #222;
        --main-text-a50: rgb(34 34 34 / 50%);
        --text-lighter-1: #383838;
        --text-lighter-2: #4a4a4a;
        --text-darker-1: #1a1a1a;
        --text-darker-2: #111;
        --medium: #585858;
        --medium-lighter-1: #686868;
        --badge-gray: var(--body-bg);
        --black-a30: rgba(0, 0, 0, 0.3);
    }

    html,
    body,
    #app {
        background-color: var(--body-bg);
        color: var(--main-text);
    }

    /* Scrollbar */
    *::-webkit-scrollbar-track{
        background-color: var(--body-bg);
    }
    *::-webkit-scrollbar-thumb{
        background-color: var(--bg-alt-5);
        border-color: var(--body-bg);
    }
    
    /* Radio button */
    .uhc-radio{
        color: var(--main-text);
    }
    .uhc-radio:hover{
        color: var(--text-darker-1);
    }
    .uhc-radio__dot{
        background-color: var(--bg-alt-1);
        border-color: var(--bg-alt-5);
    }
    .uhc-radio:hover .uhc-radio__dot{
        background-color: var(--bg-alt-1);
        border-color: var(--bg-alt-5);
    }

    /* Checkbox */
    .uhc-checkbox{
        color: var(--main-text);
    }
    .uhc-checkbox:hover{
        color: var(--text-darker-1);
    }
    .uhc-checkbox__checkmark{
        background-color: var(--bg-alt-1);
        border-color: var(--bg-alt-5);
    }
    .uhc-checkbox:hover .uhc-checkbox__checkmark{
        background-color: var(--bg-alt-1);
        border-color: var(--bg-alt-5);
    }

    /* Button */
    .uhc-button:not(.uhc-button--primary){
        color: var(--main-text);
    }
    .uhc-button--outline:hover:not(.uhc-button--disabled){
        background-color: var(--bg-alt-2);
    }
    .uhc-button__icon .uhc-icon{
        color: var(--main-text);
    }

    /* Button Secondary */
    .uhc-button--secondary:not(.uha-modules-list__item__add-platform-button){
        color: var(--main-text);
        background-color: var(--bg-alt-2);
    }
    .uhc-button--secondary:hover:not(.uhc-button--disabled):not(.uha-modules-list__item__add-platform-button){
        background-color: var(--bg-alt-3);
    }
    .uhc-button--secondary:active:not(.uhc-button--disabled):not(.uha-modules-list__item__add-platform-button){
        background-color: var(--bg-alt-5);
    }

    /* File input */
    .uhc-file-input__container-inputs{
        background-color: var(--bg-alt-1);
    }
    .uhc-file-input__container-inputs:hover{
        background-color: var(--bg-alt-2);
    }
    .uhc-file-input__container label{
        color: var(--text-lighter-1);
    }
    .uhc-file-input__container input{
        color: var(--main-text);
    }

    /* Text input */
    .uhc-input__container input{
        background-color: var(--bg-alt-1);
        color: var(--main-text);
    }
    .uhc-input__container input:hover{
        background-color: var(--bg-alt-2);
    }
    .uhc-input__container input:focus{
        background-color: var(--bg-alt-1);
    }
    .uhc-input__container label{
        color: var(--text-lighter-1);
    }

    /* Textarea */
    .uhc-textArea{
        background-color: var(--bg-alt-2);
    }
    .uhc-textArea label{
        color: var(--text-lighter-1);
    }
    .uhc-textArea:focus-within{
        background-color: var(--bg-alt-3);
    }
    .uhc-textArea textarea{
        color: var(--main-text);
    }

    /* Badge */
    .uhc-badge--grey{
        color: var(--main-text-a50);
        background-color: var(--badge-gray);
    }
    .uhc-badge--yellow{
        background-color: var(--badge-gray);
    }

    /* Context menu */
    .uhc-interactable__context-menu{
        background-color: var(--body-bg);
    }
    .uhc-interactable__section{
        border-bottom-color: var(--bg-alt-1);
    }
    .uhc-interactable__menu-item-container .uhc-interactable__menu-item .uhc-paragraph{
        color: var(--main-text);
    }

    /* Modal */
    .uhc-modal{
        background-color: var(--black-a30);
    }
    .uhc-modal .uhc-modal__container{
        background-color: var(--body-bg);
    }
    .uhc-modal .uhc-modal__container .uhc-modal__header{
        border-bottom-color: transparent;
    }
    .modal__preferences__navigation{
        border-right-color: transparent;
    }

    /* Modal header */
    .uhc-modal .uhc-modal__container .uhc-modal__header{
        color: var(--main-text);
    }

    /* Modal right column */
    .modal__learn-content-detail .uhc-modal__container .uhc-modal__body .column--right{
        background-color: transparent;
    }

    /* Drawer */
    .uha-drawer{
        background-color: var(--body-bg);
    }
    .uha-drawer__heading{
        border-bottom-color: transparent;
    }
    .uha-empty-list .uha-empty-list__title{
        color: var(--text-lighter-1);
    }
    .uha-empty-list .uha-empty-list__description{
        color: var(--main-text-a50);
    }
    .uha-drawer__overlay--open{
        background-color: var(--black-a30);
    }

    /* Header */
    .uhc-heading {
        color: var(--main-text);
    }
    .project-page-header .uhc-interactable__context-container{
        box-shadow: none;
    }

    /* Sidebar */
    .uha-navigation {
        background-color: var(--bg-alt-1);
    }

    /* Sidebar button */
    .uhc-vertical-navigation--with-icon{
        background-color: var(--bg-alt-1);
        color: var(--text-lighter-1);
    }
    .uhc-vertical-navigation--active{
        background-color: var(--bg-alt-3);
        color: var(--main-text);
    }
    .uhc-vertical-navigation:not(.uhc-vertical-navigation--active):hover{
        color: var(--text-darker-2);
    }

    /* Modal sidebar button */
    .uhc-vertical-navigation{
        color: var(--text-lighter-1);
    }

    /* Profile button */
    .uhc-profile--online, .uhc-profile--offline{
        background-color: var(--bg-alt-1);
    }
    .uhc-profile--online:hover .uhc-icon, .uhc-profile--offline:hover .uhc-icon{
        color: var(--text-darker-2);
    }

    /* Search */
    .uhc-search__container{
        background-color: var(--bg-alt-2);
    }
    .uhc-search__container:hover{
        background-color: var(--bg-alt-3);
    }
    .uhc-search__container:focus-within{
        background-color: var(--bg-alt-3);
    }
    .uhc-search__container input,
    .uhc-search__container input:focus{
        color: var(--main-text);
    }

    /* Header row */
    .pl-header__row{
        background-color: transparent;
        border-color: transparent;
    }
    .pl-header__row .pl-header__column{
        border-left-color: transparent;
    }
    .pl-header__row .pl-header__column:last-of-type{
        border-right-color: transparent;
    }
    .pl-header__row .pl-header__column:hover{
        background-color: var(--bg-alt-1);
    }
    .pl-header__row .pl-header__column:active, .pl-header__row .pl-header__column:focus{
        background-color: var(--bg-alt-2);
    }

    /* Paragraph */
    .uhc-paragraph{
        color: var(--text-lighter-1);
    }

    /* Inner link */
    .uhc-link__inner{
        color: var(--text-lighter-1);
    }

    /* Icon */
    .uhc-icon{
        color: var(--medium);
    }
    .uhc-icon-button:hover .uhc-icon{
        color: var(--text-darker-2);
    }

    /* Item row */
    .pl-item__row:hover{
        background-color: var(--bg-alt-1);
    }
    .pl-item__row:hover:not(:focus){
        box-shadow: 0 0 0 0.25rem var(--bg-alt-1);
    }
    .pl-item__row:focus{
        background-color: var(--bg-alt-2);
    }

    /* Item row button */
    .pl-item__row:hover .pl-item__column--editor .editor-version__button, .pl-item__row:hover .pl-item__advanced-button .uhc-icon-button{
        background-color: var(--bg-alt-3);
    }
    .pl-item__row:hover .pl-item__column--editor .editor-version__button:hover, .pl-item__row:hover .pl-item__advanced-button .uhc-icon-button:hover{
        background-color: var(--bg-alt-5);
    }

    /* Item row icon button */
    .pl-item__row:hover .pl-item__issues-button .uhc-icon-button{
        background-color: var(--bg-alt-3);
    }
    .pl-item__row:hover .pl-item__issues-button .uhc-icon-button:hover{
        background-color: var(--bg-alt-5);
    }

    /* Item row icon */
    .pl-item__row:hover .pl-item__column--editor .editor-version__button .uhc-icon, .pl-item__row:hover .pl-item__advanced-button .uhc-icon-button .uhc-icon{
        color: var(--main-text);
    }

    /* Dropdown button */
    .uhc-button-dropdown__button{
        color: var(--main-text);
    }
    .uhc-button-dropdown--secondary .uhc-button-dropdown__dropdown .uhc-icon{
        color: var(--main-text);
    }
    .uhc-button-dropdown--secondary .uhc-button-dropdown__button, .uhc-button-dropdown--secondary .uhc-button-dropdown__dropdown{
        background-color: var(--bg-alt-1);
    }
    .uhc-button-dropdown--secondary .uhc-button-dropdown__button:hover:not([disabled]), .uhc-button-dropdown--secondary .uhc-button-dropdown__dropdown:hover:not([disabled]){
        background-color: var(--bg-alt-2);
    }
    .uhc-button-dropdown--secondary .uhc-button-dropdown__button:active:not([disabled]), .uhc-button-dropdown--secondary .uhc-button-dropdown__dropdown:active:not([disabled]){
        background-color: var(--bg-alt-4);
    }

    /* Dropdown select */
    .uhc-dropdown__container select{
        color: var(--main-text);
        background-color: var(--bg-alt-1);
    }
    .uhc-dropdown__container select:hover{
        background-color: var(--bg-alt-2);
    }
    .uhc-dropdown__container select:focus{
        background-color: var(--bg-alt-1);
    }
    .uhc-dropdown__container label{
        color: var(--text-lighter-1);
    }

    /* Editor item */
    .editor-item{
        background-color: var(--bg-alt-1);
    }
    .editor-item:hover, .editor-item--selected{
        background-color: var(--bg-alt-2);
    }
    .editor-item:not(.editor-item--selected):hover .editor-item__radio, .editor-item:not(.editor-item--selected):hover .editor-item__radio__info__badge.uhc-badge--grey{
        color: var(--text-darker-1);
    }

    /* Editor version */
    .editor-version-item{
        background-color: var(--bg-alt-1);
        border-color: transparent;
    }
    .editor-version-item+.editor-version-item{
        border-color: transparent;
    }

    /* Editor item platform button */
    .uha-modules-list .uha-modules-list__item, .uha-modules-list .uha-modules-list__item__button, .uha-modules-list .uha-modules-list__item__add-platform-button{
        color: var(--text-lighter-1);
    }
    .uha-modules-list .uha-modules-list__item__add-platform-button{
        color: var(--body-bg);
    }

    /* License container */
    .uha-license-container{
        background-color: var(--bg-alt-1);
        border-color: var(--bg-alt-2);
    }
    .uha-license-container__badge{
        background-color: var(--bg-alt-2);
        border-right-color: transparent;
    }
    .uha-license-container__content .uha-row-container .uha-license-date .uhc-paragraph{
        color: var(--text-lighter-1);
    }

    /* License notification */
    .uhc-inline-notification__container{
        background-color: transparent;
    }
    .uhc-inline-notification__container .uhc-paragraph{
        color: var(--main-text);
    }

    /* Project issue */
    .project-issue{
        background-color: var(--body-bg);
    }

    /* Horizontal navigation */
    .uhc-horizontal-navigation{
        color: var(--main-text);
    }
    .uhc-horizontal-navigation:not(.uhc-horizontal-navigation--active):hover{
        color: var(--text-lighter-2);
    }
    .uhc-horizontal-navigation--active{
        color: var(--text-darker-2);
    }

    /* Install item */
    .uha__install-item{
        background-color: var(--bg-alt-1);
        border-color: var(--bg-alt-2);
    }
    .uha__install-item:hover{
        border-color: var(--bg-alt-5);
    }
    .uha__install-item__icon{
        background-color: var(--bg-alt-2);
    }

    /* Storage size label */
    .install-storage-requirements-container .storage-size{
        color: var(--text-lighter);
    }

    /* Add module */
    .add-module__section-head{
        background-color: var(--bg-alt-2);
    }
    .add-module__section{
        background-color: var(--bg-alt-1);
        color: var(--main-text);
    }
    .add-module__section-element{
        border-top-color: var(--bg-alt-2);
        background-color: var(--bg-alt-2);
    }
    .add-module__section-element-child:hover,
    .add-module__section-element:hover{
        background-color: var(--bg-alt-5);
    }
    .add-module__section-element-installed-item{
        background-color: var(--bg-alt-1);
    }
    .add-module__section-element-installed-item:hover{
        background-color: var(--bg-alt-1);
    }

    /* Download */
    .uha-download-group__container{
        background-color: var(--bg-alt-1);
    }
    .uha-download-item{
        background-color: var(--bg-alt-1);
    }
    .uha-download-item:hover{
        background-color: var(--bg-alt-2);
    }
    .uha-download-sub-item{
        background-color: var(--body-bg);
    }

    /* Fade container */
    .uhc-fade-image__container{
        background-color: var(--bg-alt-1);
    }

    /* Learn item */
    .uha-learn-item{
        background-color: var(--bg-alt-1);
    }
    .uha-learn-item:hover{
        background-color: var(--bg-alt-2);
    }
    .uha-learn-item__thumbnail-container{
        background-color: var(--bg-alt-1);
    }

    /* Template sidebar */
    .template-sidebar{
        background-color: var(--body-bg);
    }

    /* Template list */
    .template-list__item{
        border-color: var(--bg-alt-1);
    }
    .template-list__item--usable{
        background-color: var(--bg-alt-1);
        border-color: var(--bg-alt-1);
    }
    .template-list__item--usable:hover{
        background-color: var(--bg-alt-2);
        border-color: var(--bg-alt-2);
    }

    /* Template details */
    .modal__template-contents__info-paragraph.uhc-paragraph{
        color: var(--main-text);
    }
    .modal__template-contents .modal__template-contents__package__name{
        color: var(--main-text);
    }

    /* Template download */
    .template-preview__downloading-label{
        background-color: var(--bg-alt-1);
    }

    /* Editor selector */
    .editor-selector__container .editor-selector:hover, .editor-selector__container .editor-selector:focus{
        background-color: var(--body-bg);
    }
    .editor-list-dropdown__container{
        background-color: var(--body-bg);
    }
    .editor-list-dropdown__editor-item{
        border-bottom-color: transparent;
    }
    .editor-list-dropdown__editor-item:hover, .editor-list-dropdown__editor-item:focus{
        background-color: var(--bg-alt-1);
    }
    .editor-list-dropdown__editor-item--selected{
        background-color: var(--bg-alt-1);
    }
    .editor-list-dropdown__editor-item .uhc-heading{
        color: var(--main-text);
    }
    .editor-list-dropdown__editor-item--selected .uhc-heading{
        color: var(--text-darker-1);
    }
</style>
<script>
    let theme_options = {
        "dark": "Dark",
        "light": "Light"
    }
    const default_theme = "light";
    let last_theme = default_theme;

    document.addEventListener("click", function (event){
        if(event.target && event.target.getAttribute("data-testid") == "preferences-vertical-nav-appearance"){
            // Make sure we're not double clicking the button
            if(!document.getElementById("dropdown_theme")){
                // Delay to let the app do it's thing before we add stuff
                setTimeout(function (){
                    let appearance_container = document.querySelector(".modal__preferences__content > div");
                    if(appearance_container){
                        let last_div = document.querySelector(".modal__preferences__content > div > div:last-child");
                        last_div.classList.add("uha-menubar-container");

                        let theme_container = document.createElement("div");
                        theme_container.classList.add("uhc-dropdown__container", "uha-theme__dropdown");
                        theme_container.style = 'height: 3.375rem; margin: 1.25rem 0 1.25rem 0; width: 20rem;'

                        let h3 = document.createElement("h3");
                        h3.classList.add("uhc-heading", "uhc-heading--medium");
                        h3.innerText= 'Theme';
                        appearance_container.appendChild(h3);

                        let theme_icon = document.createElement("div");
                        theme_icon.classList.add("uhc-icon", "uhc-dropdown__container-icon");
                        theme_icon.innerHTML = '<svg height="1.5rem" width="1.5rem" viewBox="0 0 24 24"><path fill="currentColor" d="M7 10l5 5 5-5H7z"></path></svg>';
                        theme_container.appendChild(theme_icon);

                        let theme_select = document.createElement("select");
                        theme_select.id = "dropdown_theme";

                        for(const key in theme_options){
                            let theme_option = document.createElement("option");
                            theme_option.value = key;
                            theme_option.innerText = theme_options[key];
                            if(key === last_theme){
                                theme_option.selected = true;
                            }
                            theme_select.appendChild(theme_option);
                        }

                        let theme_label = document.createElement("label");
                        theme_label.htmlFor = "dropdown_theme";
                        theme_label.innerText = "Current Theme";

                        theme_container.appendChild(theme_select);
                        theme_container.appendChild(theme_label);

                        appearance_container.appendChild(theme_container);

                        theme_select.addEventListener("change", pickThemeFromEvent);
                    }
                }, 1);
            }
        }
    });

    function pickThemeFromEvent(event){
        pickTheme(event.target.value);
    }

    function pickTheme(name){
        if(last_theme){
            let last_theme_style = document.getElementById(last_theme);
            if(last_theme_style){
                last_theme_style.disabled = true;
            }
        }
        let current_theme_style = document.getElementById(name);
        if(current_theme_style){
            current_theme_style.disabled = false;
        }

        last_theme = name;
        localStorage.setItem("theme", last_theme);
    }

    let saved_theme = localStorage.getItem("theme");
    if(saved_theme === null){
        pickTheme(default_theme);
    }else{
        pickTheme(saved_theme);
    }
</script>
"""

if len(sys.argv) == 2:
    path = sys.argv[1]
    os.chdir(os.path.join(path, "resources"))
    print("Extracting app...")
    subprocess.run("npx asar extract app.asar app", shell=True)
    print("Backing up...")
    os.rename("app.asar", "app.asar.bak")
    os.chdir(os.path.join("app", "build", "renderer"))
    
    print("Patching...")
    for line in fileinput.FileInput("index.html", inplace=1):
        if "<body>" in line:
            line=line.replace(line,line + css)
        print(line, end="")
    
    print("Done! All patched. B)")
else:
    print("Incorrect arguements. Did you specify the correct path to Unity Hub?")
