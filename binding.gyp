{
  'variables': {
  },
  'targets': [
    {
      'target_name': 'nanomsg',
      'type': 'static_library',
      'defines': [
        'NN_HAVE_GCC',
        'NN_HAVE_PIPE',
        'NN_HAVE_POLL',
        'NN_USE_IFADDRS',
        'NN_HAVE_SOCKETPAIR',
        'NN_HAVE_SEMAPHORE',
        'NN_USE_PIPE',
      ],
      'conditions': [
        ['OS=="mac"', {
          'defines': [
            'NN_HAVE_CLANG',
            'NN_HAVE_OSX',
            'NN_USE_KQUEUE',
          ]
        }],
        ['OS=="linx"', {
            'NN_HAVE_LINUX',
            'NN_USE_EPOLL',
        }],
        ['OS=="win"', {
        }],
      ],

      'include_dirs': [
        'deps/nanomsg/src',
        'deps/nanomsg/src/aio',
        'deps/nanomsg/src/core',
        'deps/nanomsg/src/protocols',
        'deps/nanomsg/src/transports',
        'deps/nanomsg/src/utils',
      ],
      'sources': [
        'deps/nanomsg/src/aio/ctx.c',
        'deps/nanomsg/src/aio/fsm.c',
        'deps/nanomsg/src/aio/poller.c',
        'deps/nanomsg/src/aio/pool.c',
        'deps/nanomsg/src/aio/timer.c',
        'deps/nanomsg/src/aio/timerset.c',
        'deps/nanomsg/src/aio/usock.c',
        'deps/nanomsg/src/aio/worker.c',
        'deps/nanomsg/src/core/device.c',
        'deps/nanomsg/src/core/ep.c',
        'deps/nanomsg/src/core/epbase.c',
        'deps/nanomsg/src/core/global.c',
        'deps/nanomsg/src/core/pipe.c',
        'deps/nanomsg/src/core/poll.c',
        'deps/nanomsg/src/core/sock.c',
        'deps/nanomsg/src/core/sockbase.c',
        'deps/nanomsg/src/core/symbol.c',
        'deps/nanomsg/src/protocols/bus/bus.c',
        'deps/nanomsg/src/protocols/bus/xbus.c',
        'deps/nanomsg/src/protocols/pair/pair.c',
        'deps/nanomsg/src/protocols/pair/xpair.c',
        'deps/nanomsg/src/protocols/pipeline/pull.c',
        'deps/nanomsg/src/protocols/pipeline/push.c',
        'deps/nanomsg/src/protocols/pipeline/xpull.c',
        'deps/nanomsg/src/protocols/pipeline/xpush.c',
        'deps/nanomsg/src/protocols/pubsub/pub.c',
        'deps/nanomsg/src/protocols/pubsub/sub.c',
        'deps/nanomsg/src/protocols/pubsub/trie.c',
        'deps/nanomsg/src/protocols/pubsub/xpub.c',
        'deps/nanomsg/src/protocols/pubsub/xsub.c',
        'deps/nanomsg/src/protocols/reqrep/rep.c',
        'deps/nanomsg/src/protocols/reqrep/req.c',
        'deps/nanomsg/src/protocols/reqrep/xrep.c',
        'deps/nanomsg/src/protocols/reqrep/xreq.c',
        'deps/nanomsg/src/protocols/survey/respondent.c',
        'deps/nanomsg/src/protocols/survey/surveyor.c',
        'deps/nanomsg/src/protocols/survey/xrespondent.c',
        'deps/nanomsg/src/protocols/survey/xsurveyor.c',
        'deps/nanomsg/src/protocols/utils/dist.c',
        'deps/nanomsg/src/protocols/utils/excl.c',
        'deps/nanomsg/src/protocols/utils/fq.c',
        'deps/nanomsg/src/protocols/utils/lb.c',
        'deps/nanomsg/src/protocols/utils/priolist.c',
        'deps/nanomsg/src/transports/inproc/binproc.c',
        'deps/nanomsg/src/transports/inproc/cinproc.c',
        'deps/nanomsg/src/transports/inproc/inproc.c',
        'deps/nanomsg/src/transports/inproc/ins.c',
        'deps/nanomsg/src/transports/inproc/msgqueue.c',
        'deps/nanomsg/src/transports/inproc/sinproc.c',
        'deps/nanomsg/src/transports/ipc/aipc.c',
        'deps/nanomsg/src/transports/ipc/bipc.c',
        'deps/nanomsg/src/transports/ipc/cipc.c',
        'deps/nanomsg/src/transports/ipc/ipc.c',
        'deps/nanomsg/src/transports/ipc/sipc.c',
        'deps/nanomsg/src/transports/tcp/atcp.c',
        'deps/nanomsg/src/transports/tcp/btcp.c',
        'deps/nanomsg/src/transports/tcp/ctcp.c',
        'deps/nanomsg/src/transports/tcp/stcp.c',
        'deps/nanomsg/src/transports/tcp/tcp.c',
        'deps/nanomsg/src/transports/utils/backoff.c',
        'deps/nanomsg/src/transports/utils/dns.c',
        'deps/nanomsg/src/transports/utils/iface.c',
        'deps/nanomsg/src/transports/utils/literal.c',
        'deps/nanomsg/src/transports/utils/port.c',
        'deps/nanomsg/src/transports/utils/streamhdr.c',
        'deps/nanomsg/src/utils/alloc.c',
        'deps/nanomsg/src/utils/atomic.c',
        'deps/nanomsg/src/utils/chunk.c',
        'deps/nanomsg/src/utils/chunkref.c',
        'deps/nanomsg/src/utils/clock.c',
        'deps/nanomsg/src/utils/closefd.c',
        'deps/nanomsg/src/utils/efd.c',
        'deps/nanomsg/src/utils/err.c',
        'deps/nanomsg/src/utils/glock.c',
        'deps/nanomsg/src/utils/hash.c',
        'deps/nanomsg/src/utils/list.c',
        'deps/nanomsg/src/utils/msg.c',
        'deps/nanomsg/src/utils/mutex.c',
        'deps/nanomsg/src/utils/queue.c',
        'deps/nanomsg/src/utils/random.c',
        'deps/nanomsg/src/utils/sem.c',
        'deps/nanomsg/src/utils/sleep.c',
        'deps/nanomsg/src/utils/stopwatch.c',
        'deps/nanomsg/src/utils/thread.c',
        'deps/nanomsg/src/utils/wire.c',
      ],
      'direct_dependency_settings': {
        'include_dirs': [
          'deps/nanomsg/src'
        ]
      }
    },
    {
      'target_name': 'node_nanomsg',
      'cflags': [ '-Wall -Werror' ],
      'cflags_cc': ['-fexceptions'],
      'ldflags': ['-ldtrace'],
      'libraries': ['-ldtrace' ],
      'dependencies': [ 'nanomsg', ],
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
      ],
      'sources': [ 'src/node_nanomsg.cc' ],
      'xcode_settings': {
          'OTHER_CPLUSPLUSFLAGS': [
              '-fexceptions',
              '-Wall',
              '-Werror',
          ],
      }
    },
  ],
}
