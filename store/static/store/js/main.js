// Auto-dismiss alerts
document.addEventListener('DOMContentLoaded', () => {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(alert => {
    alert.addEventListener('click', () => alert.remove());
    setTimeout(() => {
      alert.style.transition = 'opacity .4s, transform .4s';
      alert.style.opacity = '0';
      alert.style.transform = 'translateX(60px)';
      setTimeout(() => alert.remove(), 400);
    }, 4000);
  });

  // Animate elements on scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'cardIn .5s ease both';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.product-card, .shop-card, .stat-item').forEach(el => {
    observer.observe(el);
  });

  // Price formatter
  document.querySelectorAll('.product-price').forEach(el => {
    const num = parseFloat(el.dataset.price);
    if (!isNaN(num)) {
      el.textContent = new Intl.NumberFormat('uz-UZ').format(num) + ' so\'m';
    }
  });
});
