# Aura Music — Google Stitch design prompt

Copy the following prompt into Google Stitch. It defines a functional Android
application rather than a marketing mock-up, with named screens and explicit
actions for an implementation tool to follow.

---

## Prompt

Design **Aura Music**, a polished Android offline music player with nearby P2P
music sharing. Create a connected, implementation-ready Material 3 app design
for a 360 × 800 dp Android phone. The product must work without an account or
internet connection; account features only add cloud sync.

### Visual system

* Use Material You with a deep charcoal default dark theme, a pure-black OLED
  option, and a light-theme equivalent. Let the currently playing album art
  subtly tint the primary accent color while preserving accessible contrast.
* Use a 24 dp screen gutter, 12–16 dp spacing between list items, 16 dp rounded
  cards, and clear 48 dp minimum touch targets. Use Material Symbols icons with
  visible text labels for consequential actions.
* Use a bottom navigation bar on the signed-in and guest home experience:
  **Home**, **Library**, **Share**, **Insights**, and **Profile**. Keep a
  persistent mini-player above it whenever a track is queued.
* Use realistic sample content: “Neon Hours — Sora Vale”, “Glass Tide — North
  Coast”, local/received/imported badges, file formats, durations, play counts,
  transfer size, and timestamps. Do not use lorem ipsum or decorative controls.

### Navigation and screen set

Create all screens below as separate, clearly titled mobile frames. Show
standard Android back navigation on pushed screens. Label each control by its
real action and make the destination or state change evident.

1. **Welcome and account choice**
   * Show Aura Music branding, a short offline-first explanation, and buttons:
     **Continue with Google**, **Continue with Facebook**, and **Continue as
     Guest**.
   * Add a concise privacy note: guest data stays on this device until backup is
     enabled. The social buttons lead to an account-confirmation state; Guest
     enters Home immediately.

2. **Permissions and first library scan**
   * Explain why music/media access and nearby-device permission are needed.
     Include **Allow music access**, **Set up nearby sharing**, and **Not now**.
   * After access is granted, show a scan-progress screen with indexed track
     count, storage locations, a minimum-duration selector, an **Exclude
     folders** action, and **Finish scan**.

3. **Home**
   * A greeting and sync indicator at the top, an always-visible search field,
     and a large **Shuffle library** primary action.
   * Show cards for **Continue listening**, **Recently added**, and smart
     playlists: Liked Songs, Most Played, Recently Played. Each card opens its
     detailed list; overflow menus provide Play next, Add to queue, Share, and
     Save as playlist as applicable.
   * The mini-player shows artwork, title/artist, a tappable play/pause control,
     and opens Now Playing when tapped.

4. **Library**
   * Use tabs or a segmented control for Tracks, Albums, Artists, Genres,
     Folders, and Playlists. Include source filter chips: All, Local, Received,
     Imported; and a labeled **Sort** button (Title, Date added, Duration, File
     size, Album, Play count).
   * Track rows show cover, title, artist/album, format, duration, source badge,
     and a three-dot menu with Play next, Add to queue, Add to playlist, Edit
     tags, Share, and Delete from device/library where appropriate.
   * Add a visible **Create playlist** floating action button in the Playlists
     tab. The creation sheet contains playlist name, optional description, and
     **Create playlist** / Cancel actions.

5. **Search**
   * This is opened from the global search field. Include focused search input,
     result sections for Tracks, Albums, Artists, and Playlists, plus recent
     searches with pin and clear-history controls. Results update as text is
     entered; selecting one opens its detail view.

6. **Playlist detail and queue**
   * Playlist detail includes artwork, title, track count/duration, **Play**,
     **Shuffle**, **Share playlist**, and Edit controls. Use a reorder mode with
     drag handles and a clear **Save order** button.
   * The queue screen lists current/up-next tracks with drag handles, Remove,
     **Clear queue**, and **Save queue as playlist**. An overflow menu offers
     repeat mode and smart shuffle.

7. **Now Playing and lyrics**
   * Use large album art, track metadata, favorite toggle, elapsed/remaining
     time, seek bar, previous/play-next controls, and explicit shuffle/repeat
     state. Include a waveform visualizer that reflects playback—not a static
     decoration.
   * Add action buttons: **Lyrics**, **Queue**, **Audio controls**, **Sleep
     timer**, and **More** (share, edit tags, add to playlist, trim audio).
   * The Lyrics screen shows synchronized scrolling LRC lines, highlights the
     current line, a **Find lyric file** action, and **Edit lyrics**. The edit
     screen uses editable timestamped lines and a **Save lyrics** action.

8. **Audio controls**
   * Include a 10-band equalizer with labeled frequency sliders, preset selector
     (Rock, Pop, Jazz, Bass Heavy, Classical, Acoustic, Heavy Metal, Custom),
     and **Save preset**.
   * Provide functional Bass boost, 3D virtualizer, Treble, and Volume booster
     sliders; switches for ReplayGain and Gapless playback; crossfade duration
     selector from Off to 10 seconds; and speed (0.25×–3.0×) plus pitch controls.
   * The Sleep timer sheet offers 15/30/45/60 minutes, **End of current track**,
     and **Start timer**. Show remaining time when active.

9. **Nearby Share**
   * The Share tab starts with explanatory offline status, a prominent **Find
     nearby devices** action, and secondary **Scan QR code** / **Show my QR
     code** buttons. Clearly display the required Wi-Fi Direct/Hotspot and
     Bluetooth status.
   * The discovered-devices screen lists device name, connection state, and
     **Connect** action. The QR screen has a scanner view with a Cancel button;
     the “my QR” screen shows a pairing code, device name, expiry, and **Refresh
     code**.
   * Once connected, the send flow has source tabs Tracks / Playlists, selection
     checkboxes, running total, and **Send selected**. The receive confirmation
     shows sender, number of files, size, destination, **Accept** / Decline.
   * Include an active transfer screen with per-file progress, speed, remaining
     time, Cancel, and Retry where needed. A Transfer history screen exposes
     filters (Sent, Received, Failed) and a detail view with peer, protocol,
     timestamp, total size, speed, status, and **Share log** / **Delete log**.

10. **Track detail, tags, and trimmer**
    * Track detail presents full metadata and file provenance, play count,
      completion rate, and actions for Play, Add to playlist, Share, Edit tags,
      and Trim audio.
    * Edit tags is a validated form for title, artist, album, year, track number,
      genre, and album art. Provide **Choose cover image**, **Save changes**, and
      Discard. Clearly identify editable versus read-only file properties.
    * Audio trimmer has a waveform, draggable start/end handles, exact start/end
      time fields, preview controls, output name, and **Save trimmed audio**.
      After saving, offer **Set as ringtone**, **Set as notification sound**, and
      **Set as alarm** with an Android-permission explanation.

11. **Insights and listening history**
    * Insights shows total listening time, tracks completed, skip rate, top
      artists, genres, albums, and a week/month range control. Charts must have
      readable values and accessible labels—not unexplained graphics.
    * History is reachable from Insights and contains date-grouped play events
      with time, completion percentage, and played/skipped status. Include a
      date filter, a track search, and **Clear history** confirmation.

12. **Profile, sync, settings, and backup**
    * Profile shows avatar, display name, account/guest status, listening totals,
      **Edit profile**, **Cloud backup**, and **Restore backup**. Guest users see
      a clear benefit explanation and **Sign in to sync** action.
    * Cloud backup presents last backup/sync status, data categories (playlists,
      favorites, history, preferences) as checkboxes, Wi-Fi-only switch,
      automatic backup switch, and **Back up now**. Restore uses a dated backup
      list, category selection, overwrite warning, and **Restore selected**.
    * Settings is grouped into Appearance (Light/Dark/OLED, dynamic colors),
      Library (rescan, source filter defaults, excluded folders, duration
      threshold), Playback (headphone pause/resume, gestures, crossfade),
      Sharing (device name and visibility), System integration (widget setup,
      lockscreen controls, Android Auto), and Data (export/import local backup).
      Every switch must state its effect. Export/import uses file picker states,
      validation/error feedback, and a confirmation before replacing local data.

### Functional annotations

* Treat library tracks, playlist membership/order, favorites, queue, lyrics,
  playback settings, transfer logs, listening history, profile, and backup
  preferences as dynamic persisted app state stored locally. Cloud sync is an
  optional account-backed copy of selected state.
* Show empty states with a specific recovery action—for example, “No music found
  yet” with **Scan device**, “No nearby devices” with **Scan again**, and “No
  transfers yet” with **Find nearby devices**.
* Include loading, permission-denied, transfer-failed, scan-failed, and backup
  conflict states with a clear retry, settings, cancel, or resolution action.
* Do not design as a desktop dashboard or a promotional landing page. Avoid
  unlabeled icon-only controls for primary actions, fake metrics, and buttons
  without a defined behavior. Ensure the exported frames clearly express how a
  user moves between every described screen.
