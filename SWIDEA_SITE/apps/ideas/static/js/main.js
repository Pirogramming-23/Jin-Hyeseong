function toggleStar(ideaId) {
    fetch(`/toggle_star/?id=${ideaId}`)
    .then(res => res.json())
    .then(data => {
        const btn = document.getElementById(`star-${ideaId}`);
        btn.textContent = data.is_star ? '⭐' : '☆';
    });
}
function adjustInterest(ideaId, direction) {
    fetch(`/adjust_interest/?id=${ideaId}&direction=${direction}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById(`interest-${ideaId}`).textContent = data.interest;
        });
}