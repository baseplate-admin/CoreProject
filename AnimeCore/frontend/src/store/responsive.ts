import { writable } from "svelte/store";
import { browser } from "$app/env";

function handleWindowChange(e: MediaQueryList) {
    // Check if the media query is true
    return e.matches;
}

/*
 	Mapped from here
 	https://bulma.io/documentation/helpers/visibility-helpers/
*/

const MOBILE = browser && window.matchMedia("(max-width: 768px)");
const TABLET = browser && window.matchMedia("(min-width: 769px) and (max-width: 1023px)");
const DESKTOP = browser && window.matchMedia("(min-width: 1024px) and (max-width: 1215px)");
const WIDESCREEN = browser && window.matchMedia("(min-width: 1216px) and (max-width: 1407px)");
const FULLHD = browser && window.matchMedia("(min-width: 1408px )");

// Callback function to handle changes

const checkMode = () => {
    if (handleWindowChange(MOBILE)) {
        return "mobile";
    } else if (handleWindowChange(TABLET)) {
        return "tablet";
    } else if (handleWindowChange(DESKTOP)) {
        return "desktop";
    } else if (handleWindowChange(WIDESCREEN)) {
        return "widescreen";
    } else if (handleWindowChange(FULLHD)) {
        return "fullhd";
    }
};

export const responsiveMode = writable(checkMode());

// Final event listener to handle changes

browser &&
    window?.addEventListener("resize", async () => {
        responsiveMode.update(checkMode);
    });