# Contributing Guide

본 문서는 저장소의 **브랜치 전략**, **머지 절차**, 그리고 **버전 관리 정책**을 명확히 정의하여 팀원 간 일관된 협업을 보장하기 위한 가이드라인입니다.  
모든 기여자는 아래 규칙을 준수해야 하며, 이를 위반한 코드는 `main` 및 보호 브랜치에 병합될 수 없습니다.

---

## 1. 브랜치 전략

### 1.1 주요 브랜치

- **`main`**
  - 항상 **배포 가능한 안정 상태**를 유지합니다.
  - 모든 배포 버전에는 `vX.Y.Z` 형태의 **태그**가 부여됩니다.
  - 직접 커밋/푸시는 금지되며, 반드시 Pull Request(PR)를 통해 변경됩니다.

- **`develop`**
  - 다음 릴리즈를 준비하는 **통합 개발 라인**입니다.
  - 모든 새로운 기능(`feature/*`)은 `develop`에 병합됩니다.
  - 안정화가 완료되면 `release/*` 브랜치로 분기됩니다.

### 1.2 보조 브랜치

- **`feature/*`**
  - 새로운 기능이나 실험적 작업을 위한 단기 브랜치입니다.
  - 네이밍 규칙: `feature/<scope>-<short-desc>`  
    예: `feature/perception-visibility-grid`, `feature/홍길동-yolo연동`
  - 완료 후 반드시 `develop`으로 PR을 생성하고, **Squash merge**로 병합합니다.

- **`release/*`**
  - 특정 버전 릴리즈를 준비하는 안정화 브랜치입니다.
  - 네이밍 규칙: `release/<major>.<minor>.<patch>-rc<k>`  
    예: `release/0.3.0-rc1`
  - 새로운 기능 추가는 금지되며, 버전 고정, 문서 보완, 버그 수정만 허용됩니다.
  - 안정화가 끝나면 `main`에 병합 후 태그를 생성합니다. 또한 `develop`에도 병합되어 동기화됩니다.

- **`hotfix/*`**
  - 이미 배포된 버전에서 발견된 치명적 버그 또는 보안 이슈를 즉시 수정하기 위한 브랜치입니다.
  - 네이밍 규칙: `hotfix/<version>-<issue>`  
    예: `hotfix/0.3.1-depth-scale-bug`
  - `main`에서 분기하여 수정 후, `main`에 병합 및 태그를 생성합니다.
  - 동일한 수정 사항은 반드시 `develop`에도 반영해야 합니다.

---

## 2. 머지 절차

| 소스 브랜치 | 타겟 브랜치 | 병합 방식 | 비고 |
|-------------|-------------|-----------|------|
| `feature/*` | `develop`   | **Squash merge** | 히스토리 정리 (한 기능 = 한 커밋) |
| `develop`   | `release/*` | 브랜치 생성       | 기능 동결 및 안정화 시작 |
| `release/*` | `main`      | **Merge commit** | 릴리즈 흔적 보존, 태그 필수 |
| `hotfix/*`  | `main`      | **Merge commit** | 긴급 수정, 태그 필수 |
| `main`      | `develop`   | Merge or Cherry-pick | 핫픽스 반영으로 드리프트 방지 |

> ⚠️ **주의:**  
> - `main`, `develop`, `release/*`는 보호 브랜치로 설정되며 직접 푸시가 금지됩니다.  
> - Rebase는 오직 로컬의 `feature/*` 브랜치 최신화 용도로만 사용합니다. 원격 브랜치에는 절대 rebase 하지 않습니다.

---

## 3. 커밋 규칙

### 3.1 Conventional Commits
모든 커밋은 다음 형식을 따릅니다.

```
<type>(<scope>): <description>
```

- **type**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `build`, `ci`, `chore`
- **scope**: 변경된 모듈 또는 컴포넌트 이름
- **description**: 간결한 변경 요약 (한글 또는 영문)

**예시**
- `feat(planner): add invisible-grid placement rule`
- `fix(camera): correct extrinsics axis order`
- `feat(yolo): YOLOv5 wrapper 추가`
- `fix(tracker): StrongSORT 초기화 버그 수정`

### 3.2 PR 머지 시 커밋
- `feature/*` → `develop`: **Squash merge**  
  → 결과 커밋 메시지는 해당 기능을 요약하는 한 줄로 작성합니다.
- `release/*` → `main` 또는 `hotfix/*` → `main`: **Merge commit**  
  → 릴리즈/핫픽스 이력이 명확히 남도록 합니다.

---

## 4. Pull Request 정책

- 모든 변경은 PR을 통해 이루어져야 합니다.
- **PR 제목 규칙**: `[feat] perception: add occlusion graph` 와 같이 type과 scope를 포함합니다.
- **PR 템플릿**:

```markdown
## 목적
- (한 문장) 이 PR이 해결/추가하려는 것

## 변경 사항
- feat/fix/chore 등으로 구분하여 리스트업

## 테스트
- [ ] 유닛 테스트 통과
- [ ] 로컬/시뮬 확인 (로그/스크린샷 첨부)
- [ ] 문서/예제 업데이트

## 리스크 & 롤백
- 영향 범위:
- 문제가 생기면 되돌리는 방법:

## 체크리스트
- [ ] Conventional Commit 규칙 준수
- [ ] CI 통과
- [ ] 리뷰 승인 (최소 1인)
```

---

## 5. 버전 관리
- **Semantic Versioning (SemVer)**를 준수합니다: `MAJOR.MINOR.PATCH`
  - **MAJOR**: 호환성을 깨는 변경 (ex: API 변경)
  - **MINOR**: 기능 추가 (하위 호환 유지)
  - **PATCH**: 버그 수정
- 태그는 항상 annotated 형태로 생성합니다.

```bash
git tag -a v0.3.0 -m "v0.3.0: hidden-object testbed initial release"
git push origin v0.3.0
```

- 모든 배포는 태그를 기준으로 수행됩니다.

---

## 6. 핫픽스 프로세스

1. `main`에서 새로운 `hotfix/*` 브랜치를 생성합니다.

```bash
git checkout main && git pull
git checkout -b hotfix/0.3.1-critical-fix
```

2. 수정 및 테스트 완료 후 PR을 생성합니다.
3. `main`에 병합(Merge commit)하고 태그를 생성합니다.

```bash
git checkout main && git pull
git tag -a v0.3.1 -m "v0.3.1: critical fix"
git push origin v0.3.1
```

4. 동일 수정 사항을 `develop`에도 병합(cherry-pick 또는 merge)합니다.

---

## 7. 금지/주의 사항
- ⛔ `main`, `develop`, `release/*`에 직접 푸시 금지
- ⛔ 원격 브랜치에 rebase 금지
- ⛔ feature 브랜치 장기 방치 금지 (작게 쪼개어 빠르게 병합)
- ✅ 핫픽스는 반드시 `develop`에도 반영
- ✅ 모든 PR은 CI 통과 및 리뷰 승인 후 병합

---

## 8. 빠른 명령어 요약

### 새로운 기능 개발
```bash
git checkout develop && git pull
git checkout -b feature/<scope>-<desc>
# 작업 후 PR → develop (Squash merge)
```

### 릴리즈 준비
```bash
git checkout develop && git pull
git checkout -b release/0.3.0-rc1
# 안정화 후 PR → main (Merge commit)
git tag -a v0.3.0 -m "v0.3.0"
git push origin v0.3.0
```

### 긴급 핫픽스
```bash
git checkout main && git pull
git checkout -b hotfix/0.3.1-<issue>
# 수정 후 PR → main (Merge commit)
git tag -a v0.3.1 -m "v0.3.1"
git push origin v0.3.1
# develop에도 반영
git checkout develop && git pull
git merge --no-ff origin/main
git push
```

---

## 9. CI/CD 정책

### CI 파이프라인
모든 PR은 다음 CI 체크를 통과해야 합니다:

- **Basic Check**: 저장소 구조 검증
- **Python Lint**: Flake8 기본 에러 체크
- **(선택) Code Quality**: 전체 코드 품질 검사
- **(선택) ROS 2 Build**: 패키지 빌드 테스트
- **(선택) Unit Tests**: pytest 실행

### Status Check 설정
GitHub Ruleset에 다음 Status Check를 필수로 지정:
- ✅ `Basic Check`
- ✅ `Python Lint`

---

## 10. 결론

본 규칙은 안정성(`main`), 개발 효율성(`develop`), **투명한 기록(`release`/`hotfix`)**을 보장하기 위해 제정되었습니다.
모든 팀원은 반드시 이 가이드라인을 숙지하고, PR 작성 및 머지 시 규칙을 준수해야 합니다.

---

*Last updated: 2025-10-01*
