function isScrollAtBottom() {
    return window.innerHeight + window.scrollY >= document.body.offsetHeight;
}

function loadMoreData(offset, limit) {
    const contentElement = document.querySelector(".content");
    let params = new URLSearchParams(window.location.href.split("?")[1])
    fetch(`/cards?budget=${params.get("budget")}&offset=${offset}&limit=${limit}`)
        .then(res => res.text())
        .then(html => contentElement.innerHTML += html)
}

var offset = 30
var limit = 60

window.addEventListener("scroll", () => {
    if (isScrollAtBottom()) {
        loadMoreData(offset, limit);
        offset += 30
        limit += 30
    }
});
