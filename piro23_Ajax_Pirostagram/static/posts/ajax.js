document.addEventListener('DOMContentLoaded', function () {
    // 게시물 작성 모달 show/hide
    const showBtn = document.getElementById('show-post-form-btn');
    const modal = document.getElementById('post-modal');
    const closeBtn = document.getElementById('close-post-modal');
    if (showBtn && modal && closeBtn) {
        showBtn.addEventListener('click', () => {
            modal.style.display = 'flex';
        });
        closeBtn.addEventListener('click', () => {
            modal.style.display = 'none';
        });
        window.addEventListener('click', (e) => {
            if (e.target === modal) modal.style.display = 'none';
        });
    }

    // 게시물 작성 Ajax (fetch)
    const postForm = document.getElementById('post-form');
    if (postForm) {
        postForm.addEventListener('submit', async function (e) {
            e.preventDefault();
            const formData = new FormData(postForm);
            const csrfToken = postForm.querySelector('[name=csrfmiddlewaretoken]').value;
            const res = await fetch('/posts/create/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: formData
            });
            if (res.ok) {
                // 게시물 등록 성공 시 전체 피드를 새로고침
                window.location.reload();
            } else {
                alert('게시물 작성에 실패했습니다.');
            }
        });
    }

    // 좋아요 토글 (fetch)
    document.querySelector('.feed-container').addEventListener('click', async function (e) {
        if (e.target.classList.contains('like-btn')) {
            e.preventDefault();
            const btn = e.target;
            const postId = btn.dataset.postId;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const res = await fetch(`/posts/like/${postId}/`, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrfToken, 'X-Requested-With': 'XMLHttpRequest' },
            });
            if (res.ok) {
                const data = await res.json();
                btn.innerHTML = (data.liked ? '❤️' : '🤍') + ' <span class="like-count">' + data.like_count + '</span>';
            }
        }
    });

    // 댓글 작성 (fetch)
    document.querySelector('.feed-container').addEventListener('submit', async function (e) {
        if (e.target.classList.contains('comment-form')) {
            e.preventDefault();
            const form = e.target;
            const postId = form.dataset.postId;
            const content = form.querySelector('input[name=content]').value;
            const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;
            const res = await fetch(`/posts/comment/add/${postId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: new URLSearchParams({ content })
            });
            if (res.ok) {
                const data = await res.json();
                const commentList = form.parentElement.querySelector('.comment-list');
                const div = document.createElement('div');
                div.className = 'comment-item';
                div.dataset.commentId = data.id;
                div.innerHTML = `<b>${data.username}</b>: ${data.content} <span class="comment-date">${data.created_at}</span> <button class="delete-comment-btn" data-comment-id="${data.id}">삭제</button>`;
                commentList.appendChild(div);
                form.reset();
            }
        }
    });

    // 댓글 삭제 (fetch)
    document.querySelector('.feed-container').addEventListener('click', async function (e) {
        if (e.target.classList.contains('delete-comment-btn')) {
            e.preventDefault();
            const btn = e.target;
            const commentId = btn.dataset.commentId;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const res = await fetch(`/posts/comment/delete/${commentId}/`, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrfToken, 'X-Requested-With': 'XMLHttpRequest' },
            });
            if (res.ok) {
                const data = await res.json();
                if (data.result === 'ok') {
                    btn.closest('.comment-item').remove();
                }
            }
        }
    });
}); 