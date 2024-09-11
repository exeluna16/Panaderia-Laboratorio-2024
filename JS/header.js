const header = document.getElementById('header');

header.innerHTML =`<header>
        <nav class="navbar navbar-expand-lg" style="background: #8D493A;">
            <div class="container-fluid">
                <a href="menu.html"><img src="../IMG/logo.webp" alt="logotipo" style="height: 50px; width: 50px; border-radius: 4px;"></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="#">Link</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Link-2</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Link-3</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
`;