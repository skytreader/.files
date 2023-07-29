javascript: (() => {
    const activityFeed = document.querySelector("#chrome-container > div.window-overlay > div > div > div > div.window-main-col > div:nth-child(11) > div.js-list-actions.mod-card-back");
    const activities = Array.from(activityFeed.childNodes);
    activities.reverse();
    activityFeed.append(...activities);
})();
